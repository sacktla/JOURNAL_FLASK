from flask import Flask, render_template, redirect, url_for,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from journal_database import Journal,Base
engine = create_engine('sqlite:///journal.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)



app = Flask(__name__)

@app.route('/journal/')
@app.route('/journal')
def showJournalEntries():
	#return 'This Page will show all Journal Entrie'
	session = DBSession()
	journals = session.query(Journal).all()
	
	return render_template('journals.html', journals = journals)

@app.route('/journal/<int:journal_id>/edit', methods=['GET','POST'])
def editJournalEntry(journal_id):
	session = DBSession()
	itemToEdit = session.query(Journal).filter_by(id=journal_id).one()

	if request.method == 'POST':
		if request.form['name']:
			itemToEdit.post = request.form['name']
		session.add(itemToEdit)
		session.commit()
		return redirect(url_for('showJournalEntries'))
	else:
		return render_template('journal_edit.html', item=itemToEdit)

@app.route('/journal/<int:journal_id>/delete', methods=['GET','POST'])
def deleteJournalEntry(journal_id):
	session = DBSession()
	itemToDelete = session.query(Journal).filter_by(id=journal_id).one()
	
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		return redirect(url_for('showJournalEntries'))
	else:
		return render_template('journal_delete.html', item=itemToDelete)


@app.route('/journal/new', methods=['GET', 'POST'])
def createNewJournalEntry():
	session = DBSession()
	queries = session.query(Journal).all()
	todayDate = date.today()
	posted_already = False
	for i in queries:
		if i.date == todayDate:
			posted_already = True
			break

	if request.method == 'POST':
		newItem = Journal(
			post=request.form['name'],date=date.today())
		session.add(newItem)
		session.commit()
		return redirect(url_for('showJournalEntries'))
	else:
		return render_template('journal_new.html',posted_already=posted_already)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)
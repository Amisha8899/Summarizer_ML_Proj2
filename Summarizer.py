import tkinter as tk
root = tk.Tk()
root.title("News Summariser")
root.geometry('1200x600')

tlabel = tk.Label(root,text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled' , bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

Summary = tk.Text(root, height=20, width=140)
Summary.config(state='disabled', bg='#dddddd')
Summary.pack()

salabel = tk.Label(root, text="Sentiment")
salabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext= tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarise") #give command attribute to call the function that carries out the desired functionality
btn.pack()

root.mainloop()



# you can collob the jupyter notebook with the GUI above using the function below and passing it to the command argument of the button

# def summarise():
#     url = utext.get('1.0', 'end').strip()

#     article = Article(url)
#     article.download()
#     article.parse()
#     article.nlp()

#     title.config(state='normal')
#     author.config(state='normal')
#     publication.config(state='normal')
#     Summary.config(state='normal')
#     sentiment.config(state='normal')

#     title.delete('1.0','end')
#     title.insert('1.0',article.title)

#     author.delete('1.0','end')
#     author.insert('1.0',article.authors)

#     publication.delete('1.0','end')
#     publication.insert('1.0',article.publish_date)

#     Summary.delete('1.0','end')
#     Summary.insert('1.0',article.Summary)

#     analysis = TextBlob(article.text)
#     sentiment.delete('1.0','end')
#     sentiment.insert('1.0',f'Polarity:{article.polarity}, Sentiment:{"positive" if analysis.polarity>0 else "negative" if analysis.polarity < 0 else "neutral" }')

#     title.config(state='disabled')
#     author.config(state='disabled')
#     publication.config(state='disabled')
#     Summary.config(state='disabled')
#     sentiment.config(state='disabled')



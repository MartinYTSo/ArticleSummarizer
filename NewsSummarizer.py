# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:46:17 2022

@author: Martin
"""

import tkinter as tk
import tkinter.ttk as ttk
from textblob import TextBlob
from newspaper import Article
import validators
import tkinter.messagebox
import requests

class SummarizerguiApp:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.title('News Summarizer') #title of the app
        
        self.title = ttk.Label(self.root)
        self.title.configure(text="Title") #title label
        self.title.place(anchor="nw", x=296, y=30)
        self.titleText = tk.Text(self.root,wrap=tk.WORD) 
        self.titleText.configure(background="#cacaca", height=3, width=75)
        self.titleText.place(anchor="nw", x=15, y=60)
    
        self.sumry = ttk.Label(self.root)
        self.sumry.configure(text="Summary") #summary label 
        self.sumry.place(anchor="nw", x=284, y=114)
        
        self.sumText = tk.Text(self.root, wrap=tk.WORD)
        self.sumText.configure(background="#c9c9c9", height=20, width=75)
        self.sumText.place(anchor="nw", x=15, y=145)
        
        self.urlLabel = ttk.Label(self.root)
        self.urlLabel.configure(text="URL") 
        self.urlLabel.place(anchor="nw", x=300, y=485)
        self.urlEntry = ttk.Entry(self.root) #entry box to put URL in
        self.urlEntry.place(anchor="nw", width=600, x=13, y=520)
        
        self.summarizeBut = ttk.Button(self.root, command=self.summarize)
        self.summarizeBut.configure(text="Summarize") #summarize button
        self.summarizeBut.place(anchor="nw", x=278, y=550)
        
        self.root.configure(height=800, relief="flat", width=800)
        self.root.geometry("640x600") #size of the window
        self.root.resizable(False, False)
        

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def summarize(self):
        url= self.urlEntry.get() #retrieve the URL the user entered
        valid=validators.url(url) #check if URL is valid
        if valid==True:
            try:
                article= Article(url) 
                article.download() #download article 
                article.parse()
                article.nlp()
                text=article.summary #summarize article
                self.titleText.config(state='normal')

                self.sumText.config(state='normal')

                self.titleText.delete('1.0', 'end')
                self.titleText.insert('1.0',article.title) #insert the title of article

                self.sumText.delete('1.0', 'end')
                self.sumText.insert('1.0',text) #insert the summary text of the article

                self.titleText.config(state='disabled')
                self.sumText.config(state='disabled')

            except:     
                 tkinter.messagebox.showinfo('Error', 'URL invalid, please double check your URL and try again')  #if url doesnt exist  
                    
        else:
            tkinter.messagebox.showinfo('Error', 'Please enter a valid URL') #if user does not enter a URL


if __name__ == "__main__":
    app = SummarizerguiApp()
    app.run()
 
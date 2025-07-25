import tkinter as tk
from tkinter import messagebox as mb
from mining import TwitterClientV2

root = tk.Tk()
root.title = ('X sentiment analysis')

tk.Label(root, text = 'Enter Twitter keyword or handle:').pack()
entry = tk.Entry(root, width = 50)
entry.pack()

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=500, justify = 'left').pack()

def run_analysis():
  query = entry.get()
  if not query:
    mb.showwarning('Input error, enter a valid twitter handle or keyword')
    return
  
  client = TwitterClientV2()
  tweets = client.get_tweets(query, count = 10)
  
  if not tweets:
    result_text.set('No tweets retrieved')
    return
  
  pos = len([t for t in tweets if t['sentiment'] == 'positive'])    
  neg = len([t for t in tweets if t['sentiment'] == 'negative'])
  neu = len([t for t in tweets if t['sentiment'] == 'neutral'])
  
  result = f'positive: {pos}\nNegative: {neg}\nNeutral: {neu}\nSample Tweets:\n'
  result+='\n'.join([f"{t['sentiment'].upper()}: {t['text']}" for t in tweets[:10]])
  result_text.set(result)
  
tk.Button(root, text='Analyze', command=run_analysis).pack()

root.mainloop()
  

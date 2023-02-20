# realtime-chatgpt

### ChatGPT is very cool
But it can't crawl the web. It can't get the latest information on the net.

### Idea
So I got an idea, what if I add a simple proxy program that accepts user input and will crawl data from google to get 
the articles to feed it into the conversation with ChatGPT? ChatGPT can help to generate the google query keywords
(which will be fed into the crawler) and to summarize the crawled articles.

### Challenges
The idea seemed simple enough, but I failed to notice several things:
* ChatGPT API is not ready yet, there's only the completion API
* No more free credits :(
* Too much google query will get rate limited
* I tend to overestimate man-hour when I'm excited
* I get bored easily

### Result
So, here we go, a (kinda) working implementation of the idea I had. Due to the implementation using completion API, the
app is actually very customizable (eg: can put starting context of the AI as quirky or sarcastic or naughty, etc). Some
 logics (eg: Summarization logic) are kinda wonky, but it can work. 

### Fun fact
* I think I can say about 50% of the code here are generated using ChatGPT. The rest 50% either I wrote manually (cause
asking ChatGPT is slower) or ChatGPT wrote but then refactored by me (ChatGPT is not bug-free, just like use devs). It
was fun trying to develop using (alongside) ChatGPT.
* I think `realtime` is not a suitable name, but its kinda catchy, so I'm keeping it.
* I believe some similar products (even paid ones) has the same basic idea as this. I don't believe that I'm the only 
person to think of this idea.
* This readme is fully written by me, not ChatGPT.

### Future improvements
* I made a ContextManager (actually ChatGPT made it) so that this app can run as a server serving many clients. Each
client can open multiple sessions (contexts).
* All the prompt to openai should be customizable (and made into profiles), eg: starting context prompt, context 
summarization prompt, keyword generation prompt, article summarization prompt, etc
* Maybe use the ChatGPT API project (the one that reverse engineer from the web UI)
 
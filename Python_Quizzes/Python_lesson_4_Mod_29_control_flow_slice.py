# AI Porgamming with Python: Lesson 4 Control Flow, Module 29: Break the String
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = " "

# write your loop here
for headline in headlines:
    news_ticker += headline + " " # Add headline to new_ticker
    if len(news_ticker) >= 140: # Check if length of news_ticker is >= 140 is True
        new_ticker = news_ticker[:140] # If True use slice to truncate news_ticker to 140 char
        break

print(news_ticker)
class Article:
    author = ""
    title = ""
    content = ""
    likes = 0

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:15] # slice of first 15 chars
    
# creating objects
a1 = Article()
a1.author = "John"
a1.title = "Python is awesome"
a1.content = "Some content will be here soon"
a1.like ="10"

a2 = Article()
a2.author = "Vansh"
a2.title = "JS is awesome"
a2.content = "Some content will be here soon"
a2.like = "14"

a3 = Article()
a3.author = "Amit"
a3.title = "Html is awesome"
a3.content = "Some content will be here soon"
a3.like = "20"

print("Our article are:")
print(a1)
print(a1.summary())
print(a2)
print(a2.summary())
print(a3)
print(a3.summary())
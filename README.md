# cli-count
Count things (by tag and value). Keep a simple log (.txt file).

## 0. Introduction
It's done for my personal use. It's still in progress. Feel free to contribute with suggestions, questions, code.

## 1. Docs by examples:

### 1.1. First run

No params, so help is displayed. Also the txt file is created.

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py
WARNING - Missing cli-count.txt file.
INFO - Created cli-count.txt file used to store everything.

cli-count new tag_name (start_value)       > default start_value is 0
cli-count add tag_name (value) ("a story") > default value is 1
cli-count total tag_name (start_date)      > date format: dd.mm.yyyy or today
cli-count list (tag_name) (start_date)     > date format: dd.mm.yyyy or today
cli-count tags (all)                       > show tags (with all info)
cli-count rename tag_name new_tag_name     > rename given tag
```

### 1.2. Adding a tag

Do you want to count your worked hours? Good. Create the `worked_hours` tag. Sure you can count anything you want. Negative numbers are not a problem. Use `12.345` (point) for float values.

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py new worked_hours 23
INFO - new Sun/17.09.2017/15:49:12 new worked_hours 23.0
```
### 1.3. Adding values for given tag

Now you can add your worked hours. You can use story mode (adding message for each action). Also for quick use you can use without value (default one is used: 1).

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py add worked_hours 1
INFO - add Sun/17.09.2017/15:54:42 add worked_hours 1.0 @@ 

ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py add worked_hours 2 "Fixing #12345 bug."
INFO - add Sun/17.09.2017/15:54:59 add worked_hours 2.0 @@Fixing #12345 bug. 

ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py add worked_hours 5 "Implement new feature."
INFO - add Sun/17.09.2017/15:55:19 add worked_hours 5.0 @@Implement new feature. 

ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py add worked_hours
INFO - add Sun/17.09.2017/15:55:43 add worked_hours 1.0 @@
```

### 1.4. Total

Your total worked hours:

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py total worked_hours
Sun/17.09.2017/15:49:12 new worked_hours 23.0 
Sun/17.09.2017/15:54:42 add worked_hours 1.0 @@ 
Sun/17.09.2017/15:54:59 add worked_hours 2.0 @@Fixing #12345 bug. 
Sun/17.09.2017/15:55:19 add worked_hours 5.0 @@Implement new feature. 
Sun/17.09.2017/15:55:43 add worked_hours 1.0 @@ 
INFO - TOTAL: 32.0
```

### 1.5. List

Not sure you can have a better record in reading books. :D List books I read today. Oh, maybe it's better to count pages. You can anytime make changes in `database` (it's a simple .txt file). Make sure you keep the structure.

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py list books_i_read today
INFO - Listing records...
Sun/17.09.2017/16:00:38 new books_i_read 2.0 
Sun/17.09.2017/16:01:19 add books_i_read 1.0 @@Author here - Title here. Good book. 
Sun/17.09.2017/16:01:36 add books_i_read 1.0 @@Author here - Title here. Good book, too.
```

### 1.6. Tags

You can't add values for an unknown tag. This is how you check your tags:

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py tags
INFO - Listing tags...
['worked_hours', 'books_i_read']
```

### 1.7. Rename a tag

Too long? You can rename it.

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py rename books_i_read books
INFO - Renamed: Sun/17.09.2017/16:00:38 new books 2.0 
INFO - Renamed: Sun/17.09.2017/16:01:19 add books 1.0 @@Author here - Title here. Good book. 
INFO - Renamed: Sun/17.09.2017/16:01:36 add books 1.0 @@Author here - Title here. Good book, too. 
```
And it's working. I can count the books in my bookcase now.

```
ghitabizau@notebook:~/ghita-work/cli-count$ python cli-count.py total books
Sun/17.09.2017/16:00:38 new books 2.0
Sun/17.09.2017/16:01:19 add books 1.0 @@Author here - Title here. Good book.
Sun/17.09.2017/16:01:36 add books 1.0 @@Author here - Title here. Good book, too.
Sun/17.09.2017/16:13:47 add books -1.0 @@Author here - Title here. I gave it to my friend until 25.12.2017. [ZZZ]
INFO - TOTAL: 3.0
```

## 2. Useful?

Not sure. I must try it some weeks. But it seems to be ready to be used in multiple ways as counter, log, journal, TODO list (why not?), etc. I am curious if you find new ways to use a product like this. :) Feel free to [contact me](http://ghitab.blogspot.ro/p/contact_15.html).

[![Contact me on Codementor](https://www.codementor.io/m-badges/ghitab/find-me-on-cm-b.svg)](https://www.codementor.io/@ghitab?refer=badge)

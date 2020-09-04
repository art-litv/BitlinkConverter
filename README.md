Bitlink converter
=================

Bitlink converter is an easy script wrote in Python which converts links to bitlinks.

Bitlink is a link which leads you to a webpage instead of its original link.

For example, both `bit.ly/111` and `https://www.google.com/` lead to google search page.

The script simply uses API to convert a link to a bitlink

Usage
-----

With [Bitly](https://bitly.com/) you can create bitlinks by using API

You can use bitlinks for SMM to make a shorter link for your website. With this you can increase a number of clients coming on your website. You can read more about why you should use bitlinks [here](https://bitly.com/pages/why-bitly/bitly-101)

This Python script has the following features:
if you insert a simple link you will get a bitlink. If you insert a bitlink you will get the number of times this bitlink has been clicked.

Installing
----------

To use this Python script you will need 2 libraries: requests and python-dotenv. You can install them using `pip`.

Place repository in any directory and write the path to the repository through cmd:

    cd <PATH>

Then:

    pip install -r requirements.txt

Now you can use the script through cmd. Insert your link instead of `<link>`:

    python main.py <link>

Examples
----------

`<link>` as simple link:

    C:\LinkToBitlink>python main.py https://github.com/
    Bitlink bit.ly/2DAwChO

`<link>` as bitlink

    C:\LinkToBitlink>python main.py bit.ly/2DAwChO
    Sum of clicks on the bitlink 0


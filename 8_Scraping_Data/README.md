<h1 id='summary'>Summary</h1>

-   [Web Scraping](#webscraping)

<h1 id='webscraping'>Web Scraping</h1>

[Go Back to Summary](#summary)

<h2 id='checkwebscraping'>Check What I Can Scrape</h2>

[Go Back to Summary](#summary)

-   Most of the website has a filed called `robots.txt` that describes all the data that we "can" scrape

    ```Bash
      #                      ///////
      #                     //     //
      #                    //       //
      #                   //         //                           ///             ///                      ///
      #                  //           //                                          ///                      ///
      #                 //     ///     //               //// ///  ///  /// ////   /// ////     /// ////    /// ////
      #                //   ///   ///   //            //////////  ///  ////////// ///////////  //////////  ///////////
      #               //   //       //   //          ///     ///  ///  ///        ///      /// ///     /// ///      ///
      #              //    //       //    //        ///      ///  ///  ///        ///      /// ///     /// ///      ///
      #             //      //     //      //        ///     ///  ///  ///        ///     ///  ///     /// ///     ///
      #            //        //   //        //        //////////  ///  ///        //////////   ///     /// //////////
      #            //         /////         //
      #            //         /////         //
      #             //      ///   ///      //
      #               //////         //////
      #
      #
      #    We thought you'd never make it!
      #    We hope you feel right at home in this file...unless you're a disallowed subfolder.
      #    And since you're here, read up on our culture and team: https://www.airbnb.com/careers/departments/engineering
      #    There's even a bring your robot to work day.

      User-agent: Googlebot
      Allow: /calendar/ical/
      Allow: /.well-known/amphtml/apikey.pub
      Disallow: /account
      Disallow: /alumni
      Disallow: /associates/click
      Disallow: /api/v1/trebuchet
      Disallow: /api/v3
    ```

<h2 id='beautifulsoup'>BeautifulSoup</h2>

[Go Back to Summary](#summary)

-   Before we start our project we need to install the following libraries

    ```Bash
      pip3 install beautifulsoup4
      pip3 install requests
    ```

    -   The `requests` library allows us to download the data
    -   The `beautifulsoup` library allows us to manipulate the data

-   To check the available modules, we can use `pip list`

    ```Bash
      Package                       Version
      ----------------------------- ---------
      alabaster                     0.7.12
      appnope                       0.1.0
      astroid                       2.3.3
      attrs                         19.3.0
      Babel                         2.7.0
    ```

<h3 id='beautifulbasics'>Basics</h3>

[Go Back to Summary](#summary)

```Python
  import requests
  from bs4 import BeautifulSoup

  response = requests.get('https://news.ycombinator.com/news')
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup.body)
  print(soup.body.contents)
  print(soup.find_all('div'))
  print(soup.find_all('a'))
  print(soup.title)
  print(soup.a)
  print(soup.find('a'))
  print(soup.find(id='score_14123123'))
```

-   the requests library is just like `fetch` in JavaScript, in this case we are making a `GET` request
-   The we get the response of the request using `.text`, and we use beautifulsoup to to convert into an object that we can manipulate. In this case we are using the default parser (`html.parser`)
-   We can select/target different elements
-   `soup.body`, `soup.title`, `soup.a`, `soup.find('a')`, `soup.find(id='score_14123123')` - returns the first element body
-   `soup.body.contents` - returns all the content inside `contents`
-   `soup.find_all()` - returns all the elements of a specific type
-   `soup.select('.score')` - returns all the elements that has `score` class. the `soup.select` uses css selectors to target the information. Just like `document.querySelector()`

-   With beautifulSoup we can chain our data

```Bash
  import requests
  from bs4 import BeautifulSoup

  response = requests.get('https://news.ycombinator.com/news')
  soup = BeautifulSoup(response.text, 'html.parser')
  links = soup.select('.storylink') # Get all the links
  votes = soup.select('.score') # Get all the votes
  print(votes[0].get('id')) # Get the id of the first element
  # score_24469921
```

<h3 id='simplebeautiful'>Simple Scraper</h3>

[Go Back to Summary](#summary)

-   with this simple exercise, we are going to use:

    -   `getText()` the the content of the **tag** `<tag>value</tag>`
    -   python `enumerate` to do a for loop using the **item** and **idx**
    -   python `replace('value', 'new value')`
    -   python `int()` convert into integer
    -   python `str()` convert into string

    ```Bash
      import requests
      from bs4 import BeautifulSoup
      import pprint

      def sort_stories_by_votes(list):
          return sorted(list, key=lambda k: k['votes'], reverse = True);

      def create_custom_hn():
          hn = []

          for i in range(1, 2):
              response = requests.get('https://news.ycombinator.com/news?p=' + str(i))
              soup = BeautifulSoup(response.text, 'html.parser')
              links = soup.select('.storylink')
              votes = soup.select('.score')
              subtext = soup.select('.subtext')

              for idx, item in enumerate(links):
                  title = item.getText()
                  href = item.get('href', '')
                  vote = subtext[idx].select('.score')

                  if len(vote):
                      points = int(vote[0].getText().replace(' points', ''))

                      if points > 99:
                          hn.append({'title': title, 'link': href, 'votes': points})

          return sort_stories_by_votes(hn)

      pprint.pprint(create_custom_hn())
    ```

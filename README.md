# artist2wordcloud

Simple project to learn some stuff about web scraping. Basically getting the name of an artist and scraping his azlyrics page for all of the lyrics, then returning a wordcloud. This is also a really bad idea since it makes too many requests(1 request per song). It was all fine when testing artist with 10 songs, but azlyrics wasn't really happy with the 200 requests it made when searching for the Beatles, so it banned me. At least I learned some stuff I guess.

This uses [word_cloud](https://github.com/amueller/word_cloud) to generate the wordclouds and Beautiful Soup 4 to handle the data from the pages.

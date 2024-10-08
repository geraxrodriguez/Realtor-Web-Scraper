<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!-- [![Contributors][contributors-shield]][contributors-url] -->
<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Stargazers][stars-shield]][stars-url] -->
<!-- [![Issues][issues-shield]][issues-url] -->
<!-- [![MIT License][license-shield]][license-url] -->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Real Estate Web Scraper</h3>

  <p align="center">
    Realtor Web Scraper scrapes information from Realtor.com, and then sends you an email with the top 5, cheapest, mulit-family properties in your area. 
    <br />
    <!-- <br />
    <br /> -->
    <a href="https://youtu.be/ROJaX8OCwGo">View Demo</a>
    <!-- ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

In the last lecture of CS50P, Professor Malan suggested we dive into a project we are genuinely interested in. I have aspirations to become a web developer, and I also hope to buy my first rental property soon. Learning how to web scrape a real estate website for specific information on real estate properties seemed like a good cross between those two things, and it was. My Realtor Web Scraper scrapes information from the popular website Realtor.com, and then sends me an email containing the information that was scraped.

The program begins with taking a zipcode via a command-line argument. The check_zip() function ensures the correct number of command-line arguments needed to run the program are given, and it will also check the zipcode provided is in the correct format. The zipcode can be given in either the five digit format, '12345', or the hyphenated 9-digit format, '12345-6789'

We then use the Requests first to get a response from the specified URL. The reason for the custom headers is because some websites have restricitve policies and may limit or block access to certain users, such was Realtor.com. My custom headers make my request look more like a user, e.g. someone opening the Safari browser on their macbook and typing in "Realtor.com", as opposed to a Python script. Without those custom headers, I would not get a successful response from the website.

BeautifulSoup is a great libary that makes web scraping easy, especially for a rookie like me. Making separate functions for getting the addresses, prices, and links of properties seemed like the best way to structure my program. This way, I send a request to Realtor.com, use that response to create a BeautifulSoup object, pass that object to each function, and then I search for specific classes/attribitues within that object to get the desired information. I didn't want to include all of the possible dozens of properties that could come up in a search so I sliced each list to only return information for the first 5 properties. I thought about leaving the project there, but then I thought about how cool it would be to have that information emailed to me.

The most difficult part for me about sending the email was formatting the body so that the information would be numbered for each property and group all the pieces of information pertaining to that property. I achieved this by using list comprehension, zip function, enumerate function, and join function (line 58). The program then uses MIMEtext to create the email message and sends it using smtplib.

Another challenge I came across was hiding my password. I learned how to send the email using smtplib through video tutorials. Mostly all of those tutorials explained how important it was to not hard code my email's password into the program, and a good way around this was to create an environment variable. I was able to successfully create the environment variable for my account's password, but ultimately my environment variable was not available to my program because the variable and my CS50 codespace are on different shells. That led me to creating a txt file that contains the actual password which I simply open in my program and create a variable, "pw", form its contents. I will be including that txt file in my .gitignore file, so it won't be uploaded to my repository. This means that in order to run this code yourself, you will have to create your own "password.txt" file and store your gmail password inside of there. Be sure to store that file in the same directory as the web scraper, and also safely store that txt file. If anyone is able to get access to that txt file, then they might gain access to your gmail.

The last change I decided to make was how to get the zipcode. At first, the program would ask for user input for the zipcode, via the input() function; but that meant I would have to run the program, and then type out the desired zipcode subsequently for the program to finish running. I re-wrote the program so that the zipcode was provided via sys.argv. This way, once the program is run, nothing else needs to be done.

Some limitations of this program are that it will always send the email containing the properties' information to my personal email. The program would be more dynamic if one could specify the receiving email address. It would also be awesome if the program could run on a schedule, e.g. every week, but I didn't want to pay money for the cloud schedule services that one could utilize to accomplish such task.

This was my CS50's Intro to Programming with Python final project! Thank you!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![BeautifulSoup][BeautifulSoup]][BeautifulSoup-url]
* [![Pytest][Pytest]][Pytest-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
<!-- ## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Gera Rodriguez - gerarodriguez@proton.me

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge -->
<!-- [contributors-url]: https://github.com/github_username/repo_name/graphs/contributors -->
<!-- [forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge -->
<!-- [forks-url]: https://github.com/github_username/repo_name/network/members -->
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
<!-- [issues-url]: https://github.com/github_username/repo_name/issues -->
<!-- [license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge -->
<!-- [license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ge-rar-do
<!-- [product-screenshot]: images/screenshot.png -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[BeautifulSoup]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[BeautifulSoup-url]: https://beautiful-soup-4.readthedocs.io/en/latest/
[Pytest]: https://img.shields.io/badge/Pytest-green?logo=pytest
[Pytest-url]: https://docs.pytest.org/en/stable/

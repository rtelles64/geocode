# Geocode Locator

This project is a geo-locator and search app that uses Google Maps API to generate latitudes and longitudes and then uses the Foursquare Places API to search for restaurants based on a query and the generated latitudes and longitudes.

## Getting Started

My operating system is a Mac so the installation instructions reflect this system. The code editor used was Atom. Most of the files and configurations were provided by Udacity.

### Installing Git

Git is already installed on MacOS, but these instructions are to ensure we have the latest version:

1. go to [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. download the software for Mac
3. install Git choosing all the default options

Once everything is installed, you should be able to run `git` on the command line. If usage information is displayed, we're good to go!

### Configuring Mac's Terminal (OPTIONAL)

Git can be used without reconfiguring the terminal but doing so makes it easier to use.

To configure the terminal, perform the following:

1. download [udacity-terminal-config.zip](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/March/58d31ce3_ud123-udacity-terminal-config/ud123-udacity-terminal-config.zip)
2. Move the `udacity-terminal-config` directory to the directory of your choice and name it `.udacity-terminal-config`(Note the dot in front)
3. Move the `bash-profile` to the same directory as in `step 2` and name it `.bash_profile`(Note the dot in front)
    * If you already have a `.bash_profile` file in your directory, transfer the content from the downloaded `bash_profile` to the existing `.bash_profile`

**Note:** It's considerably easier to just use
`mv bash_profile .bash_profile`
and `mv udacity-terminal-config .udacity-terminal-config`
when moving and renaming these files in order to avoid mac system errors

### First Time Git Configuration
Run each of the following lines on the command line to make sure everything is set up.
```
# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3

git config --list
```

### Git & Code Editor

The last step of configuration is to get Git working with your code editor. Below is the configuration for Atom. If you use a different editor, then do a quick search on Google for "associate X text editor with Git" (replace the X with the name of your code editor).
```
git config --global core.editor "atom --wait"
```

### Fetch the Source Code

#### Fork the starter repo
Log into your personal Github account, and fork the [geocode](https://github.com/rtelles64/geocode.git) repo so that you have a personal copy.

#### Clone the remote to your local machine
From the terminal, run the following command (be sure to replace `<username>` with your Github username):
`git clone http://github.com/<username>/geocode geocode`

This will give you a directory named `geocode` that is a clone of your remote `geocode` repository

## Version
This project uses `Python 3`

## Libararies
This project imports `httplib2` and `json`

If you do not already have these libraries installed, please run:
```
pip3 install httplib2 json
```

If this doesn't work, use:
```
sudo pip3 install httplib2 json
```

> Note: pip3 is used for python3 library installation. The standard pip install command can be used however this will install for the pre-installed Python 2 that comes with most Macs. This can be used but syntax should be changed accordingly for the code to work.

## API Keys
In order to make requests to the Google Maps API and the Foursquare Places API, you're going to have to generate an api key for Google, and a client_id and client_secret for Foursquare.

Below are the instructions to do so

### Google Maps API
You can find the general Google Maps API documentation [here](https://cloud.google.com/maps-platform/?hl=en)

First get your [Google Maps API key](https://developers.google.com/maps/documentation/geocoding/get-api-key)

The **Quick Guide** should be sufficient to generate an API key.

> Note: the api works best for this project when there are no restrictions applied to it.

#### Enable Geocoding API
After generating an api key, you'll want to [Enable the Geocoding API](https://console.developers.google.com/apis/library/geocoding-backend.googleapis.com?filter=category:maps&id=42fea2de-420b-4bd7-bd89-225be3b8b7b0&project=maps-api-1558571318343&folder&organizationId)

> Note: This may require login with your gmail account used to generate the api key

### Foursquare Places API
The general page for Foursquare's API is found [here](https://developer.foursquare.com)

Go [here](https://developer.foursquare.com/places-api) to get to the **Places API** page.

Scroll down to the **Explore Account Types** Section and click `Continue` in the **Personal** (Non-Commercial)/**Free** Card

> Note: Login here or create a new account if you haven't done so already

This directs to an **Account Verification** page but you could just click the `Return to My Apps` link at the bottom of this section

Follow the steps to creating a new app if you haven't already in order to generate a `Client ID` and `Client Secret`

### Using the Keys in the Code
Once the api keys have been generated copy and paste the keys in the variables labeled:
- `GOOGLE_API_KEY` (for Google)
- `CLIENT_ID`, `CLIENT_SECRET` (for Foursquare)

## Run geocode.py
With data loaded and with `geocode.py` in the `geocode` directory, run:

```
python geocode.py
```

or, if this doesn't work:

```
python3 geocode.py
```

This will print out a list of restaurants with their names, addresses, and an image.

> Note: If no image is given, a default one has been provided

If additional searches or additions to the printout need to be made, simply make a call to the `findRestaurant` function and pass a query (something like *tacos*) and a location (like *Los Angeles, California*)

> Note: The code is designed to return the first restaurant of a given query and location only, for simplicity.

### Using geocode.py in the Terminal
If you would like to use the geocode app in the terminal:
1. Run a Python interpreter session (using `python3` -- since this uses `Python 3`)

```
$ python3
Python 3.7.3 (default, Mar 27 2019, 09:23:15)
[Clang 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

2. Import `findRestaurant`

```
>>> from geocode import findRestaurant
```

3. Then make a new call to `findRestaurant`

```
>>> findRestaurant('tacos', 'Los Angeles, CA')

Restaurant Name: Tacos Tumbras a Tomas
Restaurant Address: 317 S Broadway (Grand Central Market, Space A-5), Los Angeles, CA 90013, United States
Image: https://fastly.4sqi.net/img/general/300x300/60270_DO0RjeY6adyK4l367F6rx-s5Dt1f1tk21t5usLOALHM.jpg

{'name': 'Tacos Tumbras a Tomas', 'address': '317 S Broadway (Grand Central Market, Space A-5), Los Angeles, CA 90013, United States', 'image': 'https://fastly.4sqi.net/img/general/300x300/60270_DO0RjeY6adyK4l367F6rx-s5Dt1f1tk21t5usLOALHM.jpg'}
```

> Note: The dictionary in the end is returned because the function itself returns a dictionary. This only happens in the interpreter

## Author(s)

* **Roy Telles, Jr.** *(with the help of the Udacity team)*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I would like to acknowledge and give big thanks to Udacity and team for this excellent resume-building experience

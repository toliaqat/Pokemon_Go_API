# Pokemon_Go_API
Pokémon GO API in Python

# IMPORTANT!
Fixed some code? Improved a function? Cleaned the mess? Other fixes? Sumbit a pull-request!

# Some Info:
1. GitHub issues are mainly for bug reporting.  
2. One goal of the project is to understand the API and to give other developers a starting point.   
3. We are discussing the release but there are some problems. One point is the usage of the Pokemon GO API. We dont want Niantic to take action against API usage. There are a lot of nice projects out there built on the API. So please dont blame us about thinking about our actions.

# Getting Started

## Step One: Install Prerequisites

1. [Install Python 2.7](https://wiki.python.org/moin/BeginnersGuide/Download)
1. [Install PIP](https://pip.pypa.io/en/stable/installing/)

## Step Two: Install Pokemon_Go_API

1. Download or clone the repository.
1. Using a terminal, navigate into the cloned repository.
1. Install all requirements for the project using `pip install -r requirements.txt`

## Step Three: Run Pokemon_Go_API

To run the project using Google login:

```bash
python ./main.py -t Google -u yourname@gmail.com -p yourpassword123 -l "123 Some Address Some City, STATE ZIP"
```

To run the project using  Pokemon Trainer Club login:

```bash
python ./main.py -t ptc -u yourusername -p yourpassword123 -l "123 Some Address Some City, STATE ZIP"
```

### Authentication Note

If you're authenticating with Google and have 2 factor authentication enabled for you account, you should
create an [application specific password](https://support.google.com/accounts/answer/185833?hl=en).


# To-Do:
- [ ] code clean up
- [x] Eat moro Protobuf..
- [x] Login as pokemon trainer + token
- [x] Login over google + token
- [x] Run to pokestops
- [x] Farm specific area for pokestops
- [x] Human walking logic
- [x] Catch Pokemon automatically
- [x] Drop items when bag is full
- [x] Scan your inventory for XYZ CP pokemon and release them
- [x] Pokemon catch filter
- [x] Hatch eggs
- [ ] Incubate eggs
- [ ] Evolve pokemons
- [ ] Use candy
- [x] Clean code
- [x] Fully automate this script
- [ ] Make v1.0 public!

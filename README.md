# CoronaVirus-A-model-for-When-you-should-close-your-office
This a model to help you and your company make a decision on whether you should open your office or send everybody home amid the COVID-19 crisis. It was first developed by [Tomas Pueyo](https://medium.com/@tomaspueyo) as a complimentary tool to his viral article on Medium [Coronavirus: Why You Must Act Now](https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca), an impressive article that I strongly recommend you read. This is a python adaptation of the model.

It's based on how many COVID-19 cases are probably in your area, and the likelihood that at least one of your employees catches it. It has lots of assumptions, but all the data necessary is [here](https://docs.google.com/spreadsheets/u/1/d/17YyCmjb2Z2QwMiRRwAb7W0vQoEAiL9Co0ARsl03dSlw/copy?usp=sharing), so you can play with the assumptions to adapt them to your situation. Note that only the necessary portions of the data were migrated to the [spread_share.csv](https://github.com/abdurahman-shiine/CoronaVirus-A-model-for-When-you-should-close-your-office) file used for this model, so you might need to get some data from the original source if you need to recompute some specific numbers.

The developed app could be used in both the English and Somali languages.

The app is live on Heroku, you can check it out [here](https://covid-19-model-2.herokuapp.com/).

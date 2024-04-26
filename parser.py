{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e3d977ba-2ac4-4790-8325-99b3bb9be4f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "\n",
    "URL = \"https://career.habr.com/vacancies/stazher\"\n",
    "file = \"information.csv\"\n",
    "\n",
    "def parser (url = URL):\n",
    "    result_list = {'href': [], 'title': [], 'overview': []}\n",
    "    x = requests.get(url)\n",
    "    soup = bs(x.text, \"html.parser\")\n",
    "    names_vacancies = soup.find_all('div', class_='vacancy-card__title')\n",
    "    vacancies_info = soup.find_all('div', class_='vacancy-card__skills')\n",
    "    for name in names_vacancies:\n",
    "        result_list['href'].append(\"https://career.habr.com/vacancies/stazher\"+ name.a['href'])\n",
    "        result_list['title'].append(name.a)\n",
    "    for info in vacancies_info:\n",
    "        result_list['overview'].append(info.text)\n",
    "    return result_list\n",
    "\n",
    "df = pd.DataFrame(data=parser())\n",
    "df.to_csv(file)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95b0d5f1-a483-4d42-9872-911904d1715b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

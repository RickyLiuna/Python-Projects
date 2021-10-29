{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib as plt\n",
    "import csv\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Country</th>\n",
       "      <th>Year</th>\n",
       "      <th>Region</th>\n",
       "      <th>Maternal mortality ratio</th>\n",
       "      <th>Proportion of births attended by skilled health personnel (%)</th>\n",
       "      <th>Infant mortality rate (deaths per 1,000 live births):::BOTHSEX</th>\n",
       "      <th>Infant mortality rate (deaths per 1,000 live births):::MALE</th>\n",
       "      <th>Infant mortality rate (deaths per 1,000 live births):::FEMALE</th>\n",
       "      <th>Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX</th>\n",
       "      <th>Under-five mortality rate, by sex (deaths per 1,000 live births):::MALE</th>\n",
       "      <th>...</th>\n",
       "      <th>Suicide mortality rate, by sex (deaths per 100,000 population):::MALE</th>\n",
       "      <th>Suicide mortality rate, by sex (deaths per 100,000 population):::FEMALE</th>\n",
       "      <th>Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX</th>\n",
       "      <th>Death rate due to road traffic injuries, by sex (per 100,000 population):::MALE</th>\n",
       "      <th>Death rate due to road traffic injuries, by sex (per 100,000 population):::FEMALE</th>\n",
       "      <th>Adolescent birth rate (per 1,000 women aged 15-19 years)</th>\n",
       "      <th>Universal health coverage (UHC) service coverage index</th>\n",
       "      <th>Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN</th>\n",
       "      <th>Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE</th>\n",
       "      <th>Health worker density, by type of occupation (per 10,000 population)::PHARMACIST</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Albania</td>\n",
       "      <td>2000</td>\n",
       "      <td>Europe</td>\n",
       "      <td>23</td>\n",
       "      <td>99.1</td>\n",
       "      <td>24.1</td>\n",
       "      <td>27.4</td>\n",
       "      <td>20.6</td>\n",
       "      <td>27.2</td>\n",
       "      <td>30.1</td>\n",
       "      <td>...</td>\n",
       "      <td>7.0</td>\n",
       "      <td>2.8</td>\n",
       "      <td>14.3</td>\n",
       "      <td>22.4</td>\n",
       "      <td>6.1</td>\n",
       "      <td>17.2</td>\n",
       "      <td>44</td>\n",
       "      <td>13.821</td>\n",
       "      <td>40.170</td>\n",
       "      <td>3.432</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Armenia</td>\n",
       "      <td>2000</td>\n",
       "      <td>Asia</td>\n",
       "      <td>43</td>\n",
       "      <td>96.8</td>\n",
       "      <td>27.0</td>\n",
       "      <td>29.8</td>\n",
       "      <td>24.1</td>\n",
       "      <td>30.7</td>\n",
       "      <td>33.8</td>\n",
       "      <td>...</td>\n",
       "      <td>5.1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>19.6</td>\n",
       "      <td>32.2</td>\n",
       "      <td>8.6</td>\n",
       "      <td>31.6</td>\n",
       "      <td>44</td>\n",
       "      <td>27.007</td>\n",
       "      <td>59.089</td>\n",
       "      <td>0.345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Armenia</td>\n",
       "      <td>2005</td>\n",
       "      <td>Asia</td>\n",
       "      <td>35</td>\n",
       "      <td>97.8</td>\n",
       "      <td>21.3</td>\n",
       "      <td>23.5</td>\n",
       "      <td>18.8</td>\n",
       "      <td>23.9</td>\n",
       "      <td>26.4</td>\n",
       "      <td>...</td>\n",
       "      <td>6.6</td>\n",
       "      <td>2.1</td>\n",
       "      <td>18.3</td>\n",
       "      <td>28.6</td>\n",
       "      <td>9.2</td>\n",
       "      <td>25.9</td>\n",
       "      <td>45</td>\n",
       "      <td>25.643</td>\n",
       "      <td>49.884</td>\n",
       "      <td>0.319</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Armenia</td>\n",
       "      <td>2010</td>\n",
       "      <td>Asia</td>\n",
       "      <td>32</td>\n",
       "      <td>99.5</td>\n",
       "      <td>16.5</td>\n",
       "      <td>18.3</td>\n",
       "      <td>14.6</td>\n",
       "      <td>18.5</td>\n",
       "      <td>20.5</td>\n",
       "      <td>...</td>\n",
       "      <td>10.5</td>\n",
       "      <td>3.5</td>\n",
       "      <td>18.0</td>\n",
       "      <td>27.7</td>\n",
       "      <td>9.5</td>\n",
       "      <td>27.1</td>\n",
       "      <td>57</td>\n",
       "      <td>28.419</td>\n",
       "      <td>52.396</td>\n",
       "      <td>0.427</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Australia</td>\n",
       "      <td>2000</td>\n",
       "      <td>Oceania</td>\n",
       "      <td>7</td>\n",
       "      <td>99.3</td>\n",
       "      <td>5.1</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.6</td>\n",
       "      <td>6.2</td>\n",
       "      <td>6.8</td>\n",
       "      <td>...</td>\n",
       "      <td>19.9</td>\n",
       "      <td>5.6</td>\n",
       "      <td>9.9</td>\n",
       "      <td>14.0</td>\n",
       "      <td>5.7</td>\n",
       "      <td>17.8</td>\n",
       "      <td>79</td>\n",
       "      <td>24.944</td>\n",
       "      <td>100.871</td>\n",
       "      <td>8.056</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Country  Year   Region  Maternal mortality ratio  \\\n",
       "0    Albania  2000   Europe                        23   \n",
       "1    Armenia  2000     Asia                        43   \n",
       "2    Armenia  2005     Asia                        35   \n",
       "3    Armenia  2010     Asia                        32   \n",
       "4  Australia  2000  Oceania                         7   \n",
       "\n",
       "   Proportion of births attended by skilled health personnel (%)  \\\n",
       "0                                               99.1               \n",
       "1                                               96.8               \n",
       "2                                               97.8               \n",
       "3                                               99.5               \n",
       "4                                               99.3               \n",
       "\n",
       "   Infant mortality rate (deaths per 1,000 live births):::BOTHSEX  \\\n",
       "0                                               24.1                \n",
       "1                                               27.0                \n",
       "2                                               21.3                \n",
       "3                                               16.5                \n",
       "4                                                5.1                \n",
       "\n",
       "   Infant mortality rate (deaths per 1,000 live births):::MALE  \\\n",
       "0                                               27.4             \n",
       "1                                               29.8             \n",
       "2                                               23.5             \n",
       "3                                               18.3             \n",
       "4                                                5.6             \n",
       "\n",
       "   Infant mortality rate (deaths per 1,000 live births):::FEMALE  \\\n",
       "0                                               20.6               \n",
       "1                                               24.1               \n",
       "2                                               18.8               \n",
       "3                                               14.6               \n",
       "4                                                4.6               \n",
       "\n",
       "   Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX  \\\n",
       "0                                               27.2                            \n",
       "1                                               30.7                            \n",
       "2                                               23.9                            \n",
       "3                                               18.5                            \n",
       "4                                                6.2                            \n",
       "\n",
       "   Under-five mortality rate, by sex (deaths per 1,000 live births):::MALE  \\\n",
       "0                                               30.1                         \n",
       "1                                               33.8                         \n",
       "2                                               26.4                         \n",
       "3                                               20.5                         \n",
       "4                                                6.8                         \n",
       "\n",
       "   ...  Suicide mortality rate, by sex (deaths per 100,000 population):::MALE  \\\n",
       "0  ...                                                7.0                       \n",
       "1  ...                                                5.1                       \n",
       "2  ...                                                6.6                       \n",
       "3  ...                                               10.5                       \n",
       "4  ...                                               19.9                       \n",
       "\n",
       "   Suicide mortality rate, by sex (deaths per 100,000 population):::FEMALE  \\\n",
       "0                                                2.8                         \n",
       "1                                                1.9                         \n",
       "2                                                2.1                         \n",
       "3                                                3.5                         \n",
       "4                                                5.6                         \n",
       "\n",
       "   Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX  \\\n",
       "0                                               14.3                                    \n",
       "1                                               19.6                                    \n",
       "2                                               18.3                                    \n",
       "3                                               18.0                                    \n",
       "4                                                9.9                                    \n",
       "\n",
       "   Death rate due to road traffic injuries, by sex (per 100,000 population):::MALE  \\\n",
       "0                                               22.4                                 \n",
       "1                                               32.2                                 \n",
       "2                                               28.6                                 \n",
       "3                                               27.7                                 \n",
       "4                                               14.0                                 \n",
       "\n",
       "   Death rate due to road traffic injuries, by sex (per 100,000 population):::FEMALE  \\\n",
       "0                                                6.1                                   \n",
       "1                                                8.6                                   \n",
       "2                                                9.2                                   \n",
       "3                                                9.5                                   \n",
       "4                                                5.7                                   \n",
       "\n",
       "   Adolescent birth rate (per 1,000 women aged 15-19 years)  \\\n",
       "0                                               17.2          \n",
       "1                                               31.6          \n",
       "2                                               25.9          \n",
       "3                                               27.1          \n",
       "4                                               17.8          \n",
       "\n",
       "   Universal health coverage (UHC) service coverage index  \\\n",
       "0                                                 44        \n",
       "1                                                 44        \n",
       "2                                                 45        \n",
       "3                                                 57        \n",
       "4                                                 79        \n",
       "\n",
       "   Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN  \\\n",
       "0                                             13.821                                 \n",
       "1                                             27.007                                 \n",
       "2                                             25.643                                 \n",
       "3                                             28.419                                 \n",
       "4                                             24.944                                 \n",
       "\n",
       "   Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE  \\\n",
       "0                                             40.170                                    \n",
       "1                                             59.089                                    \n",
       "2                                             49.884                                    \n",
       "3                                             52.396                                    \n",
       "4                                            100.871                                    \n",
       "\n",
       "   Health worker density, by type of occupation (per 10,000 population)::PHARMACIST  \n",
       "0                                              3.432                                 \n",
       "1                                              0.345                                 \n",
       "2                                              0.319                                 \n",
       "3                                              0.427                                 \n",
       "4                                              8.056                                 \n",
       "\n",
       "[5 rows x 28 columns]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv('SDG_goal3_clean.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "#selecting variables of interests (subsetting columns)\n",
    "df1=df[[\"Year\",\"Region\",\"Proportion of births attended by skilled health personnel (%)\",\"Neonatal mortality rate (deaths per 1,000 live births)\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Africa : 26.5\n",
      "Americas : 11.2\n",
      "Asia : 6.7\n",
      "Europe : 4.7\n",
      "Oceania : 3.1\n"
     ]
    }
   ],
   "source": [
    "df2=df1[df1[\"Year\"]==2015]\n",
    "df3=df2.groupby(\"Region\")\n",
    "df4=df3[\"Neonatal mortality rate (deaths per 1,000 live births)\"].max()\n",
    "last=df4.to_dict()\n",
    "for keys in last:\n",
    "  print(\"{} : {:.1F}\".format(keys,last[keys]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2005 : 55.1\n",
      "2010 : 60.8\n",
      "2015 : 39.7\n"
     ]
    }
   ],
   "source": [
    "df5=df1[df1[\"Region\"]=='Africa']\n",
    "df6=df5.groupby(\"Year\")\n",
    "df7=df6[\"Proportion of births attended by skilled health personnel (%)\"].min()\n",
    "#df7=df6[\"Neonatal mortality rate (deaths per 1,000 live births)\"].max()\n",
    "last2=df7.to_dict()\n",
    "for keys in last2:\n",
    "  print(\"{} : {:.1F}\".format(keys,last2[keys]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overall aggregate of Neonatal mortality rate accross 5 regions: 10.44\n",
      "Overall aggregate of Proportion of births attended by skilled health personnel in Africa for several years: 51.87\n"
     ]
    }
   ],
   "source": [
    "print(\"Overall aggregate of Neonatal mortality rate accross 5 regions:\",round(df4.agg(\"mean\"),2))\n",
    "print(\"Overall aggregate of Proportion of births attended by skilled health personnel in Africa for several years:\",round(df7.agg(\"mean\"),2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "df8=df[[\"Year\",\"Region\",\n",
    "        \"Neonatal mortality rate (deaths per 1,000 live births)\",\n",
    "        \"Infant mortality rate (deaths per 1,000 live births):::BOTHSEX\",\n",
    "        \"Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX\"]]\n",
    "df9=df8[df8[\"Year\"]==2015]\n",
    "df10=df9.groupby(\"Region\")\n",
    "df11=df10[\"Neonatal mortality rate (deaths per 1,000 live births)\",\n",
    "         \"Infant mortality rate (deaths per 1,000 live births):::BOTHSEX\",\n",
    "         \"Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX\"\n",
    "        ].max()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3, 4]), <a list of 5 Text xticklabel objects>)"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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wI+AnhExI5eZCfgeMTOzMpgwYcI6NTU1VwBDcIdHa1sIPFtbW3vY8OHD3650MI1x0lWFJK0eEXOBX+X33QvHR8R7TcyiBtgS+GFEPCbptxRdSoyIkBT1LPtw4HCAPn36tHwlzMxskZqamivWXXfdgT169Hi/Xbt2S7W91nILFy7U7NmzB82cOfMK0q+4VC1n29Xphvx/AjA+/59Q8L4pbwBvRMRj+f1fSEnYLEnrAeT/S30iiIjLImJERIzo0aPHsq2FmZnVGdKjR4+5TrhaX7t27aJHjx5zSL2IVc09XVUoInbL//u1cPqZkl6XtGlEPAfsCEzJfwcB5+X/f2ulkM3MrHHtnHAtP3nbVn1HkpOuKiRpy8bGR8STJczmh8D1klYFXgYOIVXImyV9D3gV2GdZYzUzM7PSOOmqTr9uZFwAOzQ1g3zz/Yh6Ru3Y0qDMzKx19D31zuGtOb/p5/3HhKbKSBp+2GGHzbr88svfAPjZz37Wc968ee0vvPDCt1ozloaceuqp65533nkzmyrXu3fvoePHj5+63nrr1ZYjrnKq+q64lVFEfLWRvyYTLjMzs2Krrrpq3HXXXWvOmDGjIh0uF1100XqVWG41cdJlZma2Emjfvn2MGTNm9rnnnrvU44Leeuutml122WWjIUOGDBwyZMjAe++9dzWAWbNmtd9pp502GjBgwKBhw4Zt9thjj3UCOP7443vtvffefUeOHLnp+uuvP/Scc85Z9ODunXbaaaPBgwcP3HjjjQdfcMEFawMcffTRvT/99NN2m2222aDRo0f3a6jcis5Jl5mZ2UripJNOevuWW27p/u6777YvHH7EEUdscPzxx8969tlnp956660vHXnkkX0BTj755F7Dhg2b//zzz085++yz3zzooIMWfcHrxRdf7Dhu3Ljnn3jiiakXXHBBr08//VQA119//fTJkydPffrpp6dceumlPWfOnNn+4osvfrNDhw4Lp02bNuW22257paFyZdwUFeF7uszMzFYS3bt3X7j33nu/e955563TqVOnhXXDH3nkkdVfeOGFTnXv582b137OnDntHn/88a5//etfXwQYPXr0h4cffnjNe++91w7ga1/72gedOnWKTp061Xbv3v3zN954o2ajjTb6/Pzzz+955513rgEwc+bMVSZPntxx3XXX/ag4llLLrUicdFWp/FM+Xwd650FvAvfkn/MxMzNrkdNOO23WlltuOWi//fZ7p25YRPDkk09O7dy5c8mPtejQocOisu3bt6e2tlZ33HFH13HjxnUdP378tK5duy4cOXLkph9//PFSV9VKLbeiWeFXsC2SNAZ4EhgFdM5/XwUm5HFmZmYt0rNnzwW77777+zfccMOi+6i22267ub/85S8X3Zf1r3/9qxPAVltt9eFVV121FqREac0116zt3r37wqXnmnzwwQftu3XrtqBr164Ln3rqqY4TJ05crW5cTU1N1F2CbKzcisw9XdXpJ8Dw4l4tSWsCjwHXVCQqMzNrFaU84mF5+slPfjJz7Nixi3525LLLLnv9sMMO6zNgwIBBCxYs0FZbbfXhNtts89r555//1gEHHNB3wIABgzp16rTw6quvfqWx+e65555zLrvssh79+/cf3L9//0+GDRu26HLhAQccMHvgwIGDhgwZMv+mm26a3lC5FZki/IDcaiPpeeCLETGnaHg3YHxEbFKOOEaMGBHjx5fyq0PlN3Ts0GaVn3TQpOUUiZnZkiRNiIglnpM4ceLE6cOGDXunoWls2U2cOHHtYcOG9a10HI1xT1d1+gXwpKR7gdfzsD7AzsDZFYvKzMzMWsz3dFWhiBhLepr8OODT/PcgMCIirq5cZGZmZtZS7umqUhHxvqR/UvDtxYh4v5IxmZmZWcs56apCkrYA/gB0A94ABKwv6QPg6BJ/8NrMzMyqiJOu6nQ1cEREPFY4UNKXgKuAYZUIark7s1vpZfv1WX5xmJmZLQe+p6s6rVaccAFExKPASvEsEzMzsxWNe7qq098l3Ul6Hlfdtxc3AMYAd1csKjMzax1ndhveuvOb0+Rzvzp37vyF+fPnP9VYmbvvvrvLMcccs2FNTU2MHz9+apcuXZr1XKmLLrpordGjR8/t27fv582ZbmXhpKsKRcSxknYF9mDJnwH6fUTcVbnIzMxsRXbNNdd0P/7442ccffTR77Vk+uuuu27tLbbY4mMnXfXz5cUqFRF/j4gjI2L3/HekEy4zM1tWd9xxR9eRI0du+vWvf71/v379Bo8ePbrfwoULufDCC9e+8847u//iF7/oPXr06H5z5sxpt/XWWw8YNGjQwAEDBgy67rrr1gB47rnnVu3fv//g/fbbb8ONN9548LbbbrvJvHnzdNVVV6357LPPdh4zZkz/zTbbbNC8efNU6XWtNk66qpCkbpLOkzRV0nuS3s2vz5O0RqXjMzOztm3q1Kmdfv/737/+4osvTn7ttdc63HfffV2OP/74d3baaacPzjnnnDduu+22Vzp37rzwzjvvfHHKlClTx40b9/zpp5++/sKF6WcXX3vttY7HHnvs2y+++OLkbt26LbjmmmvWPOSQQ94fMmTI/GuuuebladOmTWnupcmVgS8vVqebgQeAr0bETABJ6wIH53Ffq1xoZmbW1g0dOvSjjTba6HOAwYMHz3/ppZdWLS6zcOFCHXfcces/+uijXdq1a8fbb7+96htvvFED0Lt370+32Wabj01NaQ0AABdkSURBVAG+8IUvzJ8+fXqH8q5B2+Skqzr1jYjzCwfk5Os8SYdUKCYzM1tBdOjQYVEvVPv27amtrV3qUuCll17a/d13362ZNGnS1A4dOkTv3r2Hfvzxx+0AVl111cLpo264Nc4bqTq9KulkST3rBkjqKekUFn+b0czMbLmZM2dO+7XXXvvzDh06xO233971rbfeWqo3rFiXLl0WzJkzp3054muL3NNVnfYFTgXGSVonD5sF3AbsU7GozMysdZTwiIdKO+yww97bddddNx4wYMCgzTfffH6/fv0+aWqaMWPGvPPDH/5ww5NOOmlhSx45saJThLeH1W/EiBExfvz48i2wGU+kH9rMJ9JPOmhSc6MxM2sRSRMiYkThsIkTJ04fNmzYO5WKaWUwceLEtYcNG9a30nE0xpcX2xBJe0jaqtJxmJmZWfP58mLbshUwVFJNROxa6WDMzMysdE662pCIOL3SMZiZmVnL+PJiGyNp50rHYGZmZs3npKvtubLSAZiZmVnz+fJiFZJ0W0OjgLXKGYuZmZm1Didd1enLwIHAvKLhAkaWPxwzM2tNQ8cOHd6a85t00KQmn/v13HPPrbrbbrtt8sILL0yuG3b88cf36tKly4Kf//zns0pZzsiRIze94IILXt9+++3ntzTWc845Z50//vGPPYYMGTJ/3333fW/y5Mmdzj333JktnV9b4qSrOj0KzI+IccUjJD1XgXjMzMyarba2lpqaJVONK6+8ssf999//fN1vPwJzyh9ZZfierioUEbtGxD8bGLd9ueMxM7MV28iRIzc96qijeg8dOnRg3759h9x9991dAObNm6fddtutf//+/QfvvPPOG33yySeLfqPxlltuWX2LLbbYbNCgQQN33XXX/nPmzGkH0Lt376FHHXVU70GDBg384x//uGbhcr7zne/0eeONNzrsuuuum5x11lnrXHTRRWuNGTOmz7vvvtu+V69eQxcsWADA3Llz26277rqbf/rpp5o8eXKHL3/5y5sMHjx44PDhwzd96qmnOpZx07QqJ11mZmZGbW2tJk2aNPX8889//ec//3kvgAsuuGCdTp06LXz55Zcnn3POOW9NmTJlNYAZM2bUnHvuues99NBDz0+ZMmXqlltuOf/ss89e9HvBa621Vu2UKVOmHn744e8XLuOGG254bZ111vl83Lhxz59xxhlvF5RfMHDgwPl33XVXV4Cbbrqp21e+8pU5HTp0iMMOO2zDiy+++LXJkydP/dWvfvXGUUcd1byfJKkivrxoZma2EpDU6PC99977fYBtttnmo5NOOmlVgIcffrjLscce+zbAVltt9fGAAQPmAzz44IOrvfTSSx1Hjhy5GcDnn3+u4cOHL7oPecyYMe/TTHvvvff7N95445q77777hzfffHP3o48+evacOXPaPfXUU1323nvvjerKffbZZ/WvSBvgpMvMzGwl0LNnz9o5c+a0Lxz23nvvte/Xr9+nAB07dgyAmpoaFixY0GhiExFst912c2+//fZX6hvftWvXhQAvvvjiKrvtttsmAIceeujsk08+eXZD89x///0/OPvss3vPmjWr/bPPPtt59913nzt37tx2Xbt2rZ02bdqU5q1tdfLlxSolqb2k6ysdh5mZrRi6deu2cJ111vn8tttu6wowa9as9g8++GC3HXbYofib8otst912866//vruAE888UTH559/vjPAqFGjPho/fnyXZ599tgOke7CeeeaZDsXTb7zxxp9PmzZtyrRp06Y0lnDVxbf55pt/dMQRR/TZcccd59TU1NC9e/eF66+//md194YtXLiQf//7351avhUqyz1dVSoiFkjaUNKqEfFZc6eX1B4YD7wZEbtJ6gf8ifScrwnAd1syXzMzW3alPOJheRg7duwrRx99dJ+TTz55A4BTTjnlrcGDB3/aUPkTTzzx7f32269f//79B2+88cafDBo06COAXr161V566aXT99tvv/51l/vOOOOMNzfffPMG51WKffbZ5/1DDz20/x133LHom/o33njjy9///vc3PP/889erra3Vt771rfe23nrrj5dlOZWiiKh0DNYA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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = df11.plot(kind=\"bar\")\n",
    "plt.title(\"HIghest Mortality rate among neonatal, infant & under five kid accross 5 different regions in 2015\")\n",
    "plt.ylabel(\"deaths per 1,000 live births\")\n",
    "plt.legend([\"Neonatal\", \"Infant\", \"Under-five\"], loc='center left', bbox_to_anchor=(1, 0.5))\n",
    "plt.xticks(rotation=360, horizontalalignment=\"center\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "df12=df[[\"Year\",\"Region\",\n",
    "        \"Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN\",\n",
    "        \"Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE\",\n",
    "         \"Proportion of births attended by skilled health personnel (%)\"\n",
    "        ]]\n",
    "df13=df12[df12[\"Region\"]=='Africa']\n",
    "df14=df13.groupby(\"Year\")\n",
    "df15=df14[\"Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN\",\n",
    "          \"Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE\",\n",
    "          \"Proportion of births attended by skilled health personnel (%)\"\n",
    "        ].agg(\"mean\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([2004., 2006., 2008., 2010., 2012., 2014., 2016.]),\n",
       " <a list of 7 Text xticklabel objects>)"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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MAso6/ScioiIyFFLpuPElGDveOfcKmBa6rIkIiLpLBQKzZk6dWpJcXHx9HPOOWdSVVVVxrp167KLi4unH23aP/zhD4f/9Kc/HZpo/tatW7POPvvsSUe7np4smc5zK8zsl8Aj/udLgWQfAiMiItJCTk5OeO3atasBzj///Il33nnn8EsuuaSiM9L+xje+0eY9yCdMmNDw/PPPb+6MdfVUydTYr8B7TOs1/mu1P01EROSoLFiwoHrjxo05AE1NTVx88cXji4qKps+fP7+4urra3nnnnZySkpJoK/HKlSujn6+++urCY489dvrkyZNLrql4XecAAB9oSURBVLrqqrEA11133ZibbrppJMCqVatySktLJ0+ZMqWkpKRk2jvvvJMTbBlYt25d9pw5c6aUlJRMKykpmfbCCy/0A3jmmWcKTjrppClnn332pIkTJ04///zzJ4bD4a4umiPWbo3dOXcY+G//JSIiaeLrv3/7mPXlVfmdmebkUQU1P/r48duTWbahoYG//OUvAz7wgQ8cBHj33XdzH3nkkc2lpaXbzj333EmLFi0afPXVV+8vKChoWrJkSV5paWntz3/+82GXXnrpvvLy8tCzzz47ePPmzasyMjLYu3dvKDb9T33qUxOvv/768oULFx6oqamxpqYm27FjRzTujRkzpvGf//zn+vz8fLdy5cqcSy65ZNKqVavWAKxZsyZv+fLlmydMmNAwZ86cqS+88EL/D37wg9WdVU6p1G5gN7P5wM3A+ODyzrm0vkYhIiKpUVdXlzF16tQSgHnz5lVdc801e7dt25ZVWFhYV1paWgswa9asmq1bt+YAXH755Xvvv//+YSeddNL2P/3pT4PfeOONNUOHDm3KyckJX3TRRRPOO++8AxdddFFlcB0VFRUZu3btyl64cOEBgPz8/FYPHauvr7crr7xy/OrVq/MyMjLYtm1bTmTezJkzDx177LENANOnT6/ZtGlTdkoLpRMlc439AeBaYBnQlNrsiIhIV0m2Zt3ZgtfYg7Kzs6OBNxQKudra2gyAyy67rOIHP/jBmMcee6xq5syZNaNGjWoCWL58+Zqnn356wO9///vB995774jXXnttfUfycdttt40cMWJEw5NPPrklHA6Tl5c3J5DHYF5obGy0I9nW7pDMNfZK59xzzrndzrl9kVfKcyYiIoJX237f+95Xed111427/PLL9wJUVlZm7N+/P3TRRRdV3nfffdvXrl3b4pLC4MGDw6NGjap/+OGHBwHU1tZaVVVVi5hXWVkZGj16dEMoFOKee+4Z2tSUHnXXZAL7S2b2IzM7xcxmR14pz5mIiIhv4cKF+82Mj33sYwcBDhw4EDr77LOLJ0+eXHLKKadMufXWW1u1PjzyyCNbfvazn42YPHlyydy5c6du3769RSv1V7/61d2//e1vh06ZMqVk7dq1uXl5eb2nh1wbzLm2b0BkZi/Fmeycc6enJkutzZ071y1durSrVicikhbMbJlzrsWDuN5+++2txx9//N7uytORuummm0ZWVlaG7rrrrh3dnZee4O233x52/PHHT4g3L5le8e/v9ByJiIgk6ayzzjp227ZtOX//+987dA29r0rq6W5m9iFgOt594wFwzn03VZkSERGJeOGFFzZ1dx56k3avsZvZfcBFwJfxHgLzCbyhbyIiItLDJNN5rtQ5txCocM7dgvdUt8mpzZaIiIgciWQCe63/t8bMxgANwOjUZUlERESOVDLX2J8xs0HAj4A38e7cc39KcyUiIiJHpN0au3PuVufcAefck3jX1qc6525KfdZERCQdmdmcz3/+82Mjn2+66aaR11133ZjuzFM6SaYpPso5V+ecq2x/SRERkfiys7Pds88+O3jnzp1JjcyK1dDQ0NlZSisdCuwiIiJHKxQKuYULF+75/ve/PzJ23oUXXjjh17/+9eDI5/z8/FngPUp1zpw5U04//fSi4uLiGQcPHsw47bTTiqZMmVJSXFw8/f777x8M8M9//jP/xBNPnDJ9+vRpCxYsKN62bVtW121Zz3BEZ0siIpIG/vjvx7B7dac+tpURJTV85GftPlzm61//+u6ZM2dOv/nmm8uTTXr16tX5b7311jtTp06tf/DBBweNGjWq4eWXX94IsG/fvlBdXZ195StfGfe///u/G8eMGdN4//33D77++usLn3jiia1HsUW9TjKPbX0K7wlvzznn0uI+uiIi0r2GDBkS/sQnPrHv9ttvH5HsPdqPO+64Q1OnTq0HmD17du13vvOdY770pS8VXnDBBZVnn3129RtvvJG7YcOGvNNPP30yQDgcZvjw4X2u3T6ZGvs9wBXA3Wb2BPBr59y61GZLRERSLomadSp961vf2jV79uySiy++OHrv+szMTBd5ylpTUxMNDQ3Rx6Xm5+dHTwCOO+64ujfffHP1k08+OfDGG28sfPHFFw9+8pOfPFBUVFS7fPnytV26IT1MMr3iX3TOXQrMBrYCL5rZEjO7wsz63LULERHpHCNHjmz68Ic/XPHoo48Oi0wbP358/bJly/IBHn300UGJnoO+devWrIKCgvDVV1+9/7rrritfvnx5/nHHHXd4//79mS+++GI/gLq6Olu6dGluvO+ns6Q6z5nZUOBy4HPAW8BdeIH+hZTlTERE0t53vvOd8gMHDkRbj7/85S/vWbJkScGUKVNKlixZ0i9RM/2yZcvyTjjhhGlTp04tue2228bcdNNNO3Nzc91jjz226YYbbhg7ZcqUkunTp5f8/e9/7991W9MzJPPY1j8AU4CHgQedczsD85bGPhIwFfTYVhGRjkunx7ZKS0f12Fbgfufcs8EJZpbjj2lPeVAXERGR5CXTFP+9ONNe7eyMiIiIyNFLWGM3s1FAIZBnZrPwHtkKMADo3HGPIiIi0inaaor/IF6HubHAjwPTq4BvpzBPIiIicoQSBnbn3EPAQ2Z2of8AGBEREenh2mqK/7Rz7hFggpldFzvfOffjOF8TERGRbtRW57l+/t/+QEGcl4iISIeFQqE5U6dOLZkyZUpJSUnJtBdeeKEfeDedOfvssyfF+866deuy77vvviGRz3fffffQhQsXjktmfTt37szMzMyc/cMf/nB4cPoNN9wwKvJ+7969odtvv314628fmXXr1mUXFxdP76z0OiJhYHfO/dz/e0u8V9dlUURE0klOTk547dq1q9etW7f61ltvLfv2t789FmDChAkNzz///ObY5RsaGtiwYUPO7373uyGtU2vfokWLBh9//PGHnnjiiRbfv/vuu0dH3u/bty/0wAMPjDiS9Huadoe7mdkPzWyAmWWZ2V/NbI+ZfborMiciIumtsrIyNHDgwEZoWcu9++67h55++ulFJ5988uTS0tIp3/nOdwqXLl3af+rUqSW33HLLCIDy8vKsU089tXj8+PEzvvjFL45NtI4nnnhiyB133LF9165dWZs2bcoCuPrqqwvr6uoypk6dWnL++edP/NrXvjZ2+/btOVOnTi35whe+MBbgxhtvHDljxoxpkydPLrn22mvHRPI4adKk6RdffPH4oqKi6fPnzy+urq428B4ZO2XKlJIpU6aU/PjHP46eJDQ2NvKFL3xhbCStH/3oR9Fb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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax2 = df15.plot(kind=\"line\")\n",
    "plt.title(\"Average Health Profesionals Available in Africa from 2005 to 2015\")\n",
    "plt.ylabel(\"Density and %\")\n",
    "plt.legend([\"Physician\", \"Nurse\", \"Birth Attendees\"], loc='center left', bbox_to_anchor=(1, 0.5))\n",
    "plt.xticks(rotation=360, horizontalalignment=\"center\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

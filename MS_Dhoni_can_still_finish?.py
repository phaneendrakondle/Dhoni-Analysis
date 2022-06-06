{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MS Dhoni can still finish?.py",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1f1SeJV2DoNBQmeXknHhCBy1v_EX7kFGS",
      "authorship_tag": "ABX9TyNL9A/YICUU0o1qwCCYkMng",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/phaneendrakondle/Dhoni-Analysis/blob/main/MS_Dhoni_can_still_finish%3F.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IqegWjfG9PPB"
      },
      "outputs": [],
      "source": [
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "#to display all rows columns \n",
        "pd.set_option('display.max_rows', None)\n",
        "pd.set_option('display.max_columns', None)  \n",
        "pd.set_option('display.expand_frame_repr', False)\n",
        "pd.set_option('max_colwidth', -1)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv('drive/MyDrive/Colab Notebooks/IPL_ball_by_ball_updated.csv')"
      ],
      "metadata": {
        "id": "QdDWOetV9c18"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dhoni_sixes=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==6)].groupby('season')['runs_off_bat'].count())\n",
        "dhoni_fours=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==4)].groupby('season')['runs_off_bat'].count())\n",
        "dhoni_runs=pd.DataFrame(df[(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())\n",
        "dhoni_balls=pd.DataFrame(df[(df.striker=='MS Dhoni')].groupby('season')['ball'].count())\n",
        "dhoni_stats=dhoni_runs.merge(dhoni_balls,on='season')\n",
        "dhoni_stats=dhoni_stats.merge(dhoni_fours,on='season')\n",
        "dhoni_stats=dhoni_stats.merge(dhoni_sixes,on='season')\n",
        "dhoni_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored','ball':'Balls_Faced','runs_off_bat_y':'Fours','runs_off_bat':'Sixes'}, inplace = True)\n",
        "dhoni_stats['strike_rate']=100*dhoni_stats['Runs_Scored']/dhoni_stats['Balls_Faced']\n",
        "dhoni_stats"
      ],
      "metadata": {
        "id": "IcW_OaeWC-0p"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Insights from above data collected :**\n",
        "Since past couple of years, his strike rate is below 130 which indicates that his performance is low. All we know that he's a great finisher. Let's analyze his finishing skills."
      ],
      "metadata": {
        "id": "6_tfiA98XLEB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dhoni_death_sixes=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "dhoni_death_fours=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "dhoni_death_runs=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "dhoni_death_balls=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "dhoni_death_stats=dhoni_death_runs.merge(dhoni_death_balls,on='season')\n",
        "dhoni_death_stats=dhoni_death_stats.merge(dhoni_death_fours,on='season')\n",
        "dhoni_death_stats=dhoni_death_stats.merge(dhoni_death_sixes,on='season')\n",
        "dhoni_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "dhoni_death_stats['strike_rate_death']=100*dhoni_death_stats['Runs_Scored_death']/dhoni_death_stats['Balls_Faced_death']\n",
        "dhoni_death_stats['Boundaries_death']=dhoni_death_stats['Fours_death']+dhoni_death_stats['Sixes_death']\n",
        "dhoni_death_stats['Balls_per_bdry_death']=dhoni_death_stats['Balls_Faced_death']/dhoni_death_stats['Boundaries_death']\n",
        "dhoni_death_stats"
      ],
      "metadata": {
        "id": "8_1DobT2UwKx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pandya_death_sixes=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pandya_death_fours=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pandya_death_runs=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "pandya_death_balls=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "pandya_death_stats=pandya_death_runs.merge(pandya_death_balls,on='season')\n",
        "pandya_death_stats=pandya_death_stats.merge(pandya_death_fours,on='season')\n",
        "pandya_death_stats=pandya_death_stats.merge(pandya_death_sixes,on='season')\n",
        "pandya_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "pandya_death_stats['strike_rate_death']=100*pandya_death_stats['Runs_Scored_death']/pandya_death_stats['Balls_Faced_death']\n",
        "pandya_death_stats['Boundaries_death']=pandya_death_stats['Fours_death']+pandya_death_stats['Sixes_death']\n",
        "pandya_death_stats['Balls_per_bdry_death']=pandya_death_stats['Balls_Faced_death']/pandya_death_stats['Boundaries_death']\n",
        "pandya_death_stats"
      ],
      "metadata": {
        "id": "JtNfyWvaZ4E1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "russell_death_sixes=pd.DataFrame(df[(df.striker=='AD Russell')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "russell_death_fours=pd.DataFrame(df[(df.striker=='AD Russell')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "russell_death_runs=pd.DataFrame(df[(df.striker=='AD Russell')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "russell_death_balls=pd.DataFrame(df[(df.striker=='AD Russell')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "russell_death_stats=russell_death_runs.merge(russell_death_balls,on='season')\n",
        "russell_death_stats=russell_death_stats.merge(russell_death_fours,on='season')\n",
        "russell_death_stats=russell_death_stats.merge(russell_death_sixes,on='season')\n",
        "russell_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "russell_death_stats['strike_rate_death']=100*russell_death_stats['Runs_Scored_death']/russell_death_stats['Balls_Faced_death']\n",
        "russell_death_stats['Boundaries_death']=russell_death_stats['Fours_death']+russell_death_stats['Sixes_death']\n",
        "russell_death_stats['Balls_per_bdry_death']=russell_death_stats['Balls_Faced_death']/russell_death_stats['Boundaries_death']\n",
        "russell_death_stats"
      ],
      "metadata": {
        "id": "29AfotpfwzS-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pollard_death_sixes=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pollard_death_fours=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pollard_death_runs=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "pollard_death_balls=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "pollard_death_stats=pollard_death_runs.merge(pollard_death_balls,on='season')\n",
        "pollard_death_stats=pollard_death_stats.merge(pollard_death_fours,on='season')\n",
        "pollard_death_stats=pollard_death_stats.merge(pollard_death_sixes,on='season')\n",
        "pollard_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "pollard_death_stats['strike_rate_death']=100*pollard_death_stats['Runs_Scored_death']/pollard_death_stats['Balls_Faced_death']\n",
        "pollard_death_stats['Boundaries_death']=pollard_death_stats['Fours_death']+pollard_death_stats['Sixes_death']\n",
        "pollard_death_stats['Balls_per_bdry_death']=pollard_death_stats['Balls_Faced_death']/pollard_death_stats['Boundaries_death']\n",
        "pollard_death_stats"
      ],
      "metadata": {
        "id": "dS7TtZXVxOMz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "abd_death_sixes=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "abd_death_fours=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "abd_death_runs=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "abd_death_balls=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "abd_death_stats=abd_death_runs.merge(abd_death_balls,on='season')\n",
        "abd_death_stats=abd_death_stats.merge(abd_death_fours,on='season')\n",
        "abd_death_stats=abd_death_stats.merge(abd_death_sixes,on='season')\n",
        "abd_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "abd_death_stats['strike_rate_death']=100*abd_death_stats['Runs_Scored_death']/abd_death_stats['Balls_Faced_death']\n",
        "abd_death_stats['Boundaries_death']=abd_death_stats['Fours_death']+abd_death_stats['Sixes_death']\n",
        "abd_death_stats['Balls_per_bdry_death']=abd_death_stats['Balls_Faced_death']/abd_death_stats['Boundaries_death']\n",
        "abd_death_stats"
      ],
      "metadata": {
        "id": "6HTwsK0nzbjN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pant_death_sixes=pd.DataFrame(df[(df.striker=='RR Pant')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pant_death_fours=pd.DataFrame(df[(df.striker=='RR Pant')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())\n",
        "pant_death_runs=pd.DataFrame(df[(df.striker=='RR Pant')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())\n",
        "pant_death_balls=pd.DataFrame(df[(df.striker=='RR Pant')&(df.ball>16)].groupby('season')['ball'].count())\n",
        "pant_death_stats=pant_death_runs.merge(pant_death_balls,on='season')\n",
        "pant_death_stats=pant_death_stats.merge(pant_death_fours,on='season')\n",
        "pant_death_stats=pant_death_stats.merge(pant_death_sixes,on='season')\n",
        "pant_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)\n",
        "pant_death_stats['strike_rate_death']=100*pant_death_stats['Runs_Scored_death']/pant_death_stats['Balls_Faced_death']\n",
        "pant_death_stats['Boundaries_death']=pant_death_stats['Fours_death']+pant_death_stats['Sixes_death']\n",
        "pant_death_stats['Balls_per_bdry_death']=pant_death_stats['Balls_Faced_death']/pant_death_stats['Boundaries_death']\n",
        "pant_death_stats"
      ],
      "metadata": {
        "id": "a1S4xvDIemL7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dff=pd.merge(dhoni_death_stats.Balls_per_bdry_death,pant_death_stats.Balls_per_bdry_death,how='left',on='season')\n",
        "dff.rename(columns = {'Balls_per_bdry_death_x':'DHONI','Balls_per_bdry_death_y':'PANT'}, inplace = True)\n",
        "dff=pd.merge(dff,abd_death_stats.Balls_per_bdry_death,how='left',on='season')\n",
        "dff=pd.merge(dff,pandya_death_stats.Balls_per_bdry_death,how='left',on='season')\n",
        "dff.rename(columns = {'Balls_per_bdry_death_x':'ABD','Balls_per_bdry_death_y':'HARDIK'}, inplace = True)\n",
        "dff=pd.merge(dff,pollard_death_stats.Balls_per_bdry_death,how='left',on='season')\n",
        "dff=pd.merge(dff,russell_death_stats.Balls_per_bdry_death,how='left',on='season')\n",
        "dff.rename(columns = {'Balls_per_bdry_death_x':'POLLARD','Balls_per_bdry_death_y':'RUSSELL'}, inplace = True)\n",
        "\n",
        "dff"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 520
        },
        "id": "x4FnQLpgfTzN",
        "outputId": "bdd63415-5787-494b-b2d9-616e5ab801b9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           DHONI      PANT       ABD    HARDIK    POLLARD   RUSSELL\n",
              "season                                                             \n",
              "2008    3.583333 NaN       NaN       NaN       NaN        NaN      \n",
              "2009    4.642857 NaN        3.235294 NaN       NaN        NaN      \n",
              "2010    2.538462 NaN       NaN       NaN        2.689655  NaN      \n",
              "2011    3.233333 NaN        4.000000 NaN        5.083333  NaN      \n",
              "2012    6.222222 NaN        2.571429 NaN        4.272727   4.666667\n",
              "2013    3.909091 NaN        2.440000 NaN        3.806452  NaN      \n",
              "2014    4.303030 NaN        3.150000 NaN        6.312500  NaN      \n",
              "2015    4.240000 NaN        2.470588  2.785714  3.851852   3.500000\n",
              "2016    4.000000  4.000000  3.066667 NaN        4.846154   4.153846\n",
              "2017    4.941176  2.571429  2.375000  4.857143  5.615385  NaN      \n",
              "2018    3.685714  2.285714  2.428571  6.285714  11.500000  2.851852\n",
              "2019    4.343750  2.708333  2.875000  3.225000  3.565217   2.509804\n",
              "2020    4.357143  3.727273  3.185185  3.241379  2.967742  NaN      \n",
              "2021    3.923077  5.142857  2.961538  4.181818  4.611111   4.250000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5e8c389b-306a-491d-97c0-9e5594709e8c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>DHONI</th>\n",
              "      <th>PANT</th>\n",
              "      <th>ABD</th>\n",
              "      <th>HARDIK</th>\n",
              "      <th>POLLARD</th>\n",
              "      <th>RUSSELL</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>season</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2008</th>\n",
              "      <td>3.583333</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2009</th>\n",
              "      <td>4.642857</td>\n",
              "      <td>NaN</td>\n",
              "      <td>3.235294</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2010</th>\n",
              "      <td>2.538462</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2.689655</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2011</th>\n",
              "      <td>3.233333</td>\n",
              "      <td>NaN</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>5.083333</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012</th>\n",
              "      <td>6.222222</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2.571429</td>\n",
              "      <td>NaN</td>\n",
              "      <td>4.272727</td>\n",
              "      <td>4.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2013</th>\n",
              "      <td>3.909091</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2.440000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>3.806452</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2014</th>\n",
              "      <td>4.303030</td>\n",
              "      <td>NaN</td>\n",
              "      <td>3.150000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>6.312500</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2015</th>\n",
              "      <td>4.240000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2.470588</td>\n",
              "      <td>2.785714</td>\n",
              "      <td>3.851852</td>\n",
              "      <td>3.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>4.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>3.066667</td>\n",
              "      <td>NaN</td>\n",
              "      <td>4.846154</td>\n",
              "      <td>4.153846</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2017</th>\n",
              "      <td>4.941176</td>\n",
              "      <td>2.571429</td>\n",
              "      <td>2.375000</td>\n",
              "      <td>4.857143</td>\n",
              "      <td>5.615385</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018</th>\n",
              "      <td>3.685714</td>\n",
              "      <td>2.285714</td>\n",
              "      <td>2.428571</td>\n",
              "      <td>6.285714</td>\n",
              "      <td>11.500000</td>\n",
              "      <td>2.851852</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019</th>\n",
              "      <td>4.343750</td>\n",
              "      <td>2.708333</td>\n",
              "      <td>2.875000</td>\n",
              "      <td>3.225000</td>\n",
              "      <td>3.565217</td>\n",
              "      <td>2.509804</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>4.357143</td>\n",
              "      <td>3.727273</td>\n",
              "      <td>3.185185</td>\n",
              "      <td>3.241379</td>\n",
              "      <td>2.967742</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2021</th>\n",
              "      <td>3.923077</td>\n",
              "      <td>5.142857</td>\n",
              "      <td>2.961538</td>\n",
              "      <td>4.181818</td>\n",
              "      <td>4.611111</td>\n",
              "      <td>4.250000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5e8c389b-306a-491d-97c0-9e5594709e8c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5e8c389b-306a-491d-97c0-9e5594709e8c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5e8c389b-306a-491d-97c0-9e5594709e8c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Above we have got the data about the balls per boundary by few of the top finishers  ABD,PANT,RUSSELL,PANDYA,POLLY. Among all these we can clearly see that the balls per boundary around 3 indicates a sublime form of finishing the innings but unlike this, dhoni never been to that figure in his career. So, let's analyze his strike rate as well."
      ],
      "metadata": {
        "id": "bWdLOCdBra8h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "death_17runs=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())\n",
        "death_17balls=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())\n",
        "death_17out=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())\n",
        "death_17runs.rename(columns={'runs_off_bat':'over_17_runs'},inplace=True)\n",
        "death_17balls.rename(columns={'ball':'over_17_balls'},inplace=True)\n",
        "death_17_stats=death_17runs.merge(death_17balls,on='season')\n",
        "death_17_stats['SR']=100*death_17_stats['over_17_runs']/death_17_stats['over_17_balls']\n",
        "death_17_stats = pd.merge(death_17_stats, death_17out, how='left', on='season')\n",
        "death_17_stats"
      ],
      "metadata": {
        "id": "BNknNgh4HiL4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ax = plt.gca()\n",
        "death_17_stats.plot(kind = 'bar',\n",
        "        y = 'SR',\n",
        "        color = 'green',ax = ax)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "s2Bv4pJ-PupY",
        "outputId": "73d41ccf-b585-4b23-9eee-f73fc12c3219"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Overs 17 :** we can see that his strike rate in past five seasons is not impressive"
      ],
      "metadata": {
        "id": "037i28Rrxb8p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "death_18runs=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())\n",
        "death_18balls=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())\n",
        "death_18out=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())\n",
        "death_18runs.rename(columns={'runs_off_bat':'over_18_runs'},inplace=True)\n",
        "death_18balls.rename(columns={'ball':'over_18_balls'},inplace=True)\n",
        "death_18_stats=death_18runs.merge(death_18balls,on='season')\n",
        "death_18_stats['SR']=100*death_18_stats['over_18_runs']/death_18_stats['over_18_balls']\n",
        "death_18_stats = pd.merge(death_18_stats, death_18out, how='left', on='season')\n",
        "death_18_stats"
      ],
      "metadata": {
        "id": "Wv83ArQ9Ogr7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ax = plt.gca()\n",
        "death_18_stats.plot(kind = 'bar',\n",
        "        y = 'SR',\n",
        "        color = 'green',ax = ax)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "cmvPFrdSQCt9",
        "outputId": "42d6b30d-9e68-428d-e80c-859fbc8e88e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Over 18 :** Strike Rate hardly touches 140 to 150 in over 18 which is considerable."
      ],
      "metadata": {
        "id": "18OenctvxtW9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "death_19runs=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())\n",
        "death_19balls=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())\n",
        "death_19out=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())\n",
        "death_19runs.rename(columns={'runs_off_bat':'over_19_runs'},inplace=True)\n",
        "death_19balls.rename(columns={'ball':'over_19_balls'},inplace=True)\n",
        "death_19_stats=death_19runs.merge(death_19balls,on='season')\n",
        "death_19_stats['SR']=100*death_19_stats['over_19_runs']/death_19_stats['over_19_balls']\n",
        "death_19_stats = pd.merge(death_19_stats, death_19out, how='left', on='season')\n",
        "death_19_stats"
      ],
      "metadata": {
        "id": "Xvv4T1x7OjDZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ax = plt.gca()\n",
        "death_19_stats.plot(kind = 'bar',\n",
        "        y = 'SR',\n",
        "        color = 'green',ax = ax)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "l1GaYLSBQKT1",
        "outputId": "42dd6255-11cc-4a68-af49-e1a1ce7a2f8b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Over 19 :** He's very poor striking in this over throughout his career."
      ],
      "metadata": {
        "id": "yhCwYmAyx8GZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "death_20runs=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())\n",
        "death_20balls=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())\n",
        "death_20out=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())\n",
        "death_20runs.rename(columns={'runs_off_bat':'over_20_runs'},inplace=True)\n",
        "death_20balls.rename(columns={'ball':'over_20_balls'},inplace=True)\n",
        "death_20_stats=death_20runs.merge(death_20balls,on='season')\n",
        "death_20_stats['SR']=100*death_20_stats['over_20_runs']/death_20_stats['over_20_balls']\n",
        "death_20_stats = pd.merge(death_20_stats, death_20out, how='left', on='season')\n",
        "death_20_stats"
      ],
      "metadata": {
        "id": "RJMsFgj4OlXX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "RctvFm8BFsAU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ax = plt.gca()\n",
        "death_20_stats.plot(kind = 'bar',\n",
        "        y = 'SR',\n",
        "        color = 'green',ax = ax)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "D4WpaPtlQP8l",
        "outputId": "79b7b1a1-77c6-48aa-d219-d7e851592fa7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Over 20 :** The above visualization shows how he got transformed as a final over specialist. His strikes almost at 250."
      ],
      "metadata": {
        "id": "oJSHFio4yGpI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Conclusion:**\n",
        "\n",
        "Dhoni is not the one who keeps striking all over the death overs, his balls per boundary is around 4 which is not a great stat to consider. Interestingly, he never touched 3(which is a best rate) in his career throughout. But he has the ability to play a finisher role even at this stage. We have seen how hard he is going after the ball in 20th over (SR almost 250) and still maintains it consistently over past 5 years. His age is not a factor. One thing I can conclude is that he can't play a finisher who can hit right from 16-20 overs but has the ability to finish the innings high."
      ],
      "metadata": {
        "id": "Y-yBwDMByeVw"
      }
    }
  ]
}
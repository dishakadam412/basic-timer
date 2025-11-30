{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPFIK3LLQnYk4mL4/QAU26S",
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
        "<a href=\"https://colab.research.google.com/github/dishakadam412/basic-timer/blob/main/timer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2JPXSkJGbgHE"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "\n",
        "my_time = int(input(\"Enter the time in seconds: \"))\n",
        "\n",
        "## asks users how long they want the timer to be\n",
        "\n",
        "for i in range(my_time, 0, -1):\n",
        "  seconds = i % 60\n",
        "  minutes = int(i/60)%60\n",
        "  hours = int(i/3600)\n",
        "  print(f\"{hours:02}:{minutes:02}:{seconds:02}\")\n",
        "  time.sleep(1)\n",
        "\n",
        "## converts the given number into however long the timer will be\n",
        "## ex: one hour, two minutes, etc. and will count down by one second.\n",
        "\n",
        "print(\"TIMES UP\")\n",
        "\n",
        "## Marks end of timer"
      ]
    }
  ]
}
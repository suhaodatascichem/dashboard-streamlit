{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/suhaodatascichem/dashboard-streamlit/blob/main/dashboard_sbm_final.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Load dataset\n",
        "url = 'https://github.com/suhaodatascichem/dashboard-streamlit/raw/refs/heads/main/Soybean%20meal.xlsx'\n",
        "@st.cache_data\n",
        "def load_data():\n",
        "    return pd.read_excel(url, engine=\"openpyxl\")\n",
        "\n",
        "df = load_data()"
      ],
      "metadata": {
        "id": "0klHj2V5a1Kp",
        "outputId": "9472153d-d90a-49cb-e10d-ed0f3f9cb6da",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-13 14:33:24.646 No runtime found, using MemoryCacheStorageManager\n",
            "2025-03-13 14:33:24.649 No runtime found, using MemoryCacheStorageManager\n",
            "2025-03-13 14:33:24.650 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:24.651 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:24.651 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:25.158 Thread 'Thread-10': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:25.159 Thread 'Thread-10': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:51.244 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:33:51.245 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Sidebar options\n",
        "st.sidebar.header(\"Chart Settings\")\n",
        "chart_type = st.sidebar.selectbox(\"Select Chart Type\", [\"Scatter Plot\", \"Bar Chart\"])\n",
        "\n",
        "# Column selection\n",
        "numeric_columns = df.select_dtypes(include=['number']).columns.tolist()\n",
        "\n",
        "if len(numeric_columns) < 2:\n",
        "    st.error(\"Dataset must contain at least two numeric columns for visualization.\")\n",
        "else:\n",
        "    x_axis = st.sidebar.selectbox(\"Select X-Axis\", numeric_columns)\n",
        "    y_axis = st.sidebar.selectbox(\"Select Y-Axis\", numeric_columns)\n",
        "\n",
        "    # Generate chart\n",
        "    st.title(\"📊 Data Visualization Dashboard\")\n",
        "\n",
        "    if chart_type == \"Scatter Plot\":\n",
        "        fig = px.scatter(df, x=x_axis, y=y_axis, title=f\"Scatter Plot: {x_axis} vs {y_axis}\")\n",
        "        st.plotly_chart(fig, use_container_width=True)\n",
        "\n",
        "    elif chart_type == \"Bar Chart\":\n",
        "        fig = px.bar(df, x=x_axis, y=y_axis, title=f\"Bar Chart: {x_axis} vs {y_axis}\")\n",
        "        st.plotly_chart(fig, use_container_width=True)\n",
        "\n",
        "    # Show dataset preview\n",
        "    with st.expander(\"🔍 View Dataset\"):\n",
        "        st.write(df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RFp7NFZ14U0a",
        "outputId": "01ff32c4-9b3d-47c6-b640-7008a338e710"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-13 14:24:23.759 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.761 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.763 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.764 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.764 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.775 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.776 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.777 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.778 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.782 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.783 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.787 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.788 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.865 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.870 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.871 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.882 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-13 14:24:23.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}
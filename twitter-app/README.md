# Twitter Sentiment Analysis

Real-time Twitter sentiment analysis application with both command-line and GUI interfaces using Twitter API v2.

## Features

- **Real-time Twitter data retrieval** using Twitter API v2
- **Dual interfaces**: Command-line and GUI (Tkinter) applications
- **Text preprocessing** with regex pattern cleaning
- **Sentiment classification** using TextBlob (positive/negative/neutral)
- **Statistical analysis** with percentage breakdown
- **Sample display** of tweets for each sentiment category
- **Secure API management** with environment variables

## Technologies Used

- Python 3.x
- Tweepy (Twitter API v2)
- TextBlob (Sentiment Analysis)
- Tkinter (GUI)
- Regular Expressions

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Silas-TA/twitter-app.git
cd twitter-app
```

### 2. Install Dependencies

```bash
pip install tweepy textblob
```

### 3. Set Up Twitter API Access

1. Create a Twitter Developer account at [developer.twitter.com](https://developer.twitter.com/)
2. Create a new app and get your Bearer Token
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` and add your Bearer Token:
   ```
   TWITTER_BEARER_TOKEN=your_actual_bearer_token_here
   ```

### 4. Run the Application

**Command Line Interface:**

```bash
python mining.py
```

**GUI Interface:**

```bash
python gui_app.py
```

## Usage

- **CLI**: Modify the query in `main()` function in `mining.py`
- **GUI**: Enter any keyword or Twitter handle in the input field and click "Analyze"

## Security Note

- Never commit your `.env` file or API keys to version control
- The `.env` file is ignored by git for security
- Use the provided `.env.example` as a template

## Sample Output

```
Positive: 33.33%
Negative: 26.67%
Neutral: 40.00%
```

## License

MIT License

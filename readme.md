# Flask NBA Chatbot Assistant

Tapi Goredema, Nathan Kim, Edward Cho-Jung, Joseph Lee

A simple Flask-based chatbot that answers questions using:

1. **Local CSV dataset** (`player_data.csv` → cleaned by `etl.py` → `local_data.csv`)  
2. **BallDon’tLie API** for live **player profile** info (jersey number, college, draft pick)

---

## 🚀 Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/DataProject2.git
   cd DataProject2


2. **Install Dependencies if Needed**

3. **run python app.py and python etl.py**

4. **export BALLDONTLIE_API_KEY=3756e490-28d6-4a44-9851-37b6e4757270**

5. **example chatbot commands**
    curl -X POST http://127.0.0.1:8080/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"who is the heaviest player?"}'
    
    curl -X POST http://127.0.0.1:8080/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"what college has the most players?"}'


    curl -X POST http://127.0.0.1:8080/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"player info stephen curry"}'


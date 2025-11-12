

📁 File Transfer System (Client–Server using TCP)

A simple file transfer system built using Python TCP sockets.
This project allows a client to download files from a server over a reliable TCP connection.

🚀 Features

🔗 TCP-based reliable connection between client and server

📂 File transfer in chunks (supports large files)

💾 Files automatically saved in received/ folder

🧩 Modular and easy-to-extend architecture

✅ Simple command-line interface for learning and testing

🧠 How to Use

1️⃣ Start the server:

python server.py


2️⃣ Start the client:

python client.py


3️⃣ When prompted, enter the exact filename you want to download:

Enter filename to download: example.txt


✅ The file will be saved automatically in the received/ folder.

⚙️ How It Works

The client connects to the server using TCP sockets.

The client sends the name of the file it wants.

The server reads the requested file in chunks and sends it over the socket.

The client receives the chunks and reconstructs the full file locally.

Once the transfer completes, both client and server close the connection gracefully.

🌟 Possible Extensions

🧵 Support multiple simultaneous clients using multithreading

🔐 Add authentication and encrypted file transfers (SSL/TLS)

🪟 Create a GUI for easy file browsing and transfer

⏯️ Add resume capability for interrupted downloads

🗂️ Add file management features (upload/delete/list files)

🤝 Contribution Guidelines

Feel free to fork this repository and submit pull requests to improve it.
For major changes, please open an issue first to discuss your ideas.

👨‍💻 Author

Aman Kumar Kasaudhan (2023021210)
Ashish Kumar Yadav(2023021221)
Chandan Gupta(2023021225)
📧 cgupta7068@gmail.com
]
🌐 https://github.com/cgupta7068/FileTransfer.git

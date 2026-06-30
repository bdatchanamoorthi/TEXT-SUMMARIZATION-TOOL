AI Text Summarization Tool

A simple Python-based AI application that generates concise summaries from long text using the Hugging Face Transformers library and the facebook/bart-large-cnn model.

 Features
 Summarize manually entered text
 Read text directly from a .txt file
 Powered by Facebook's BART Large CNN model
 Fast and accurate abstractive summarization
Simple command-line interface (CLI)
 Technologies Used
Python 3.x
Hugging Face Transformers
PyTorch
Facebook BART Large CNN Model
 Project Structure
.
├── sum.py          # Main application
├── README.md       # Project documentation
└── requirements.txt
 Installation

Clone the repository:

git clone https://github.com/bdatchanamoorthi/text-summarizer.git
cd text-summarizer

Install dependencies:

pip install transformers torch
Usage

Run the application:

python sum.py

Choose one of the following options:

1. Enter text manually
2. Read from a TXT file

The application will generate a concise summary if the input text is long enough.

 Example

Input

Artificial Intelligence is transforming healthcare by improving diagnosis, treatment planning, and patient monitoring...

Output

AI is revolutionizing healthcare through improved diagnosis, treatment planning, and patient care.
Model Used
facebook/bart-large-cnn
Transformer-based abstractive text summarization model from Hugging Face.
 Future Improvements
Web-based interface using FastAPI or Flask
PDF and DOCX document support
Adjustable summary length
Multi-language summarization
Export summaries to PDF or TXT
Batch document summarization
 Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

 License

This project is licensed under the MIT License.

 Author

Datchana moorthi B

AI & Machine Learning Enthusiast
Python Developer

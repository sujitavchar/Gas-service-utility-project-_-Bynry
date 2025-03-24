\documentclass{article}
\usepackage{hyperref}
\usepackage{listings}

\title{Gas Utility Service Management API}
\author{Django REST Framework (DRF) Application}
\date{}

\begin{document}

\maketitle

\section{📌 Features}

\begin{itemize}
    \item Customers can \textbf{create service requests} with details and file attachments.
    \item Customers can \textbf{track request status} (Pending, In Progress, Resolved).
    \item Support representatives can \textbf{update and manage service requests}.
    \item RESTful API with \textbf{GET, POST, PUT, DELETE} endpoints.
    \item Uses \texttt{.env} for environment variables \& security.
    \item Docker support for easy deployment.
\end{itemize}

\section{📂 Project Structure}

\begin{lstlisting}
gas-utility-api/
│── config/                  # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│── customers/               # Customer management app
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│── service_requests/        # Service request management app
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│── .env                     # Environment variables
│── manage.py                # Django management script
│── requirements.txt         # Dependencies list
│── Dockerfile               # Docker setup
│── README.md                # Documentation (this file)
\end{lstlisting}

\section{📦 Installation \& Setup}

\subsection{1️⃣ Clone the Repository}
\begin{lstlisting}
git clone https://github.com/yourusername/gas-utility-api.git
cd gas-utility-api
\end{lstlisting}

\subsection{2️⃣ Set Up a Virtual Environment}
\begin{lstlisting}
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
\end{lstlisting}

\subsection{3️⃣ Install Dependencies}
\begin{lstlisting}
pip install -r requirements.txt
\end{lstlisting}

\subsection{4️⃣ Create .env File}
\begin{lstlisting}
touch .env  # macOS/Linux
echo > .env  # Windows
\end{lstlisting}

Add the following variables:
\begin{lstlisting}
SECRET_KEY="your-django-secret-key"
DEBUG=True
\end{lstlisting}

\subsection{5️⃣ Apply Migrations}
\begin{lstlisting}
python manage.py migrate
\end{lstlisting}

\subsection{6️⃣ Run the Development Server}
\begin{lstlisting}
python manage.py runserver
\end{lstlisting}

\textbf{API Base URL:} \url{http://127.0.0.1:8000/}  
\textbf{Django Admin Panel:} \url{http://127.0.0.1:8000/admin/}

\section{🚀 API Endpoints}

\subsection{Customer Management}

\begin{tabular}{|c|l|l|}
\hline
\textbf{Method} & \textbf{Endpoint} & \textbf{Description} \\ \hline
GET    & \texttt{/api/customers/}         & List all customers     \\ \hline
POST   & \texttt{/api/customers/}         & Create a new customer  \\ \hline
GET    & \texttt{/api/customers/\{id\}/}  & Retrieve a customer    \\ \hline
PUT    & \texttt{/api/customers/\{id\}/}  & Update customer details \\ \hline
DELETE & \texttt{/api/customers/\{id\}/}  & Delete a customer      \\ \hline
\end{tabular}

\subsection{Service Requests}

\begin{tabular}{|c|l|l|}
\hline
\textbf{Method} & \textbf{Endpoint} & \textbf{Description} \\ \hline
GET    & \texttt{/api/service-requests/}         & List all service requests \\ \hline
POST   & \texttt{/api/service-requests/}         & Create a new request      \\ \hline
GET    & \texttt{/api/service-requests/\{id\}/}  & Retrieve a request        \\ \hline
PUT    & \texttt{/api/service-requests/\{id\}/}  & Update request status     \\ \hline
DELETE & \texttt{/api/service-requests/\{id\}/}  & Delete a request          \\ \hline
\end{tabular}

\textbf{Test API in browser:} \url{http://127.0.0.1:8000/api/}
 

\end{document}


# Todo App with Flask and React

This is a simple Todo application built with Flask (backend) and React (frontend). It uses Tailwind CSS for styling, Radix UI for simple components, and shadcn for more complex components.

## Prerequisites

- Python 3.7+
- Node.js 14+
- npm or yarn

## Setup

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

The backend will be running on `http://localhost:5000`.

### Frontend

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```
   npm start
   # or
   yarn start
   ```

The frontend will be running on `http://localhost:3000`.

## Development

To work on this application, you'll need to have both the backend and frontend running simultaneously:

1. Start the backend Flask server in one terminal window.
2. Start the frontend development server in another terminal window.

The frontend will proxy API requests to the backend, so you can develop both parts of the application seamlessly.

## Building for Production

To build the frontend for production:

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Run the build command:
   ```
   npm run build
   # or
   yarn build
   ```

This will create a `dist` directory with the compiled and optimized frontend assets. You can then serve these static files using a web server of your choice, or integrate them with your Flask application for a combined deployment.

## Project Structure

- `backend/`: Contains the Flask application and SQLite database
- `frontend/`: Contains the React application and all frontend-related files
  - `src/`: Source code for the React application
    - `components/`: React components
    - `App.tsx`: Main application component
    - `index.tsx`: Entry point for the React application
  - `public/`: Public assets
  - `package.json`: Frontend dependencies and scripts
  - `tsconfig.json`: TypeScript configuration
  - `vite.config.ts`: Vite configuration
  - `tailwind.config.js`: Tailwind CSS configuration 
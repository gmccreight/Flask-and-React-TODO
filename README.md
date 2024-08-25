# Todo App with Flask and React

This is a simple Todo application built with Flask (backend) and React
(frontend). It uses Tailwind CSS for styling, Radix UI for simple components,
and shadcn to generate more complex components.

## Prerequisites

- Python 3.7+
- Node.js 14+
- npm

## Setup

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

The backend will be running on `http://localhost:5002`.

### Frontend

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

The frontend will be running on `http://localhost:3002`.

### Frontend with Tailwind CSS

To add additional shadcn components, run:

```
npx shadcn-ui@latest init
```

That adds the `frontend/components.json` file with the options you chose.

Then you can add a component, like how we added a card, to the frontend by running:

```
npx shadcn-ui@latest add card
```

Which added a card component to the `frontend/src/components/ui/card.tsx` file.

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
   ```

This will create a `dist` directory with the compiled and optimized frontend assets. You can then serve these static files using a web server of your choice, or integrate them with your Flask application for a combined deployment.

To view the production build in your browser, run:
```
npm run preview
```

## Project Structure

- `backend/`: Contains the Flask application and SQLite database
- `frontend/`: Contains the React application and all frontend-related files
  - `src/`: Source code for the React application
    - `components/`: React components
    - `App.tsx`: Main application component
    - `index.tsx`: Entry point for the React application
  - `package.json`: Frontend dependencies and scripts
  - `tsconfig.json`: TypeScript configuration
  - `vite.config.ts`: Vite configuration
  - `tailwind.config.js`: Tailwind CSS configuration 
## Frontend

It uses React with TypeScript, Tailwind CSS for styling, Radix UI for simple components, and shadcn to generate more complex components.

### Setup

The setup was taken care of by the .devcontainer

### Running

`npm start`

The frontend will be running on `http://localhost:3002`.


### Testing

To run the tests in the frontend directory, run:
```
npm test
```

There's not much to test, but it shows how to test a React application.

### Adding components

This is what we did at first to add additional shadcn components.  We ran:

```
npx shadcn-ui@latest init
```

That adds the `frontend/components.json` file with the options you chose (which is
in our version control already).

Then you can add a component, like how we added a card, to the frontend by running:

```
npx shadcn-ui@latest add card
```

Which added a card component to the `frontend/src/components/ui/card.tsx` file.


### Building for Production

`npm run build`

This will create a `dist` directory with the compiled and optimized frontend
assets. You can then serve these static files using a web server of your choice,
or integrate them with your FastAPI application for a combined deployment.

To view the production build in your browser, run:
```
npm run preview
```

### Project Structure

- `src/`: Source code for the React application
  - `components/`: React components
  - `App.tsx`: Main application component
  - `index.tsx`: Entry point for the React application
- `package.json`: Frontend dependencies and scripts
- `tsconfig.json`: TypeScript configuration
- `vite.config.ts`: Vite configuration
- `tailwind.config.js`: Tailwind CSS configuration 
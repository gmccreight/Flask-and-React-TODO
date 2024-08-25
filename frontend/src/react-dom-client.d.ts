declare module 'react-dom/client' {
  import * as ReactDOM from 'react-dom';
  export const createRoot: typeof ReactDOM.createRoot;
  export const hydrateRoot: typeof ReactDOM.hydrateRoot;
}
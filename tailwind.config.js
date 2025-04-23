/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}", // ← important!
    ],
    theme: {
      extend: {
        colors: {
          primary: '#800020',
          accent: '#f7e7ce',
          background: '#f5f5f5',
          text: '#2e2e2e',
        },
      },
    },
    plugins: [],
  }
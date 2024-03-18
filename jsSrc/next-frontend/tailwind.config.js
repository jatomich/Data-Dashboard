/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{html,js,ts,jsx,tsx}", "./components/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    colors: {
        transparent: 'transparent',
        current: 'currentColor',
        white: '#dbeafe',
        red: '#ef4444',
        indigo: '#6366f1'
        },
    extend: {},
  },
  plugins: [],
}


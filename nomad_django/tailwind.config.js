module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing:{
        "25vh" : "25vh",
        "50vh" : "50vh",
        "75vh" : "75vh",
      },
      borderRadius: {
        xl : "1.5rem"
      },
      fontWeight: ['hover', 'focus'],
      minHeight: {
        '0': '0',
        '25vh': '25vh',
        '50vh': '50vh',
        '75vh': '75vh',
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

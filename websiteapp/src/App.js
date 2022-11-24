import Slider from './Slider';
import Box from './Box';
import './App.css';
import { useState } from 'react';

function App() {
  const [red, setRed] = useState(0);
  const [green, setGreen] = useState(0);
  const [blue, setBlue] = useState(0);

  return (
    <div className="App">
      <Slider
        color = {"Red"}
        red = {red}
        setRed = {setRed}
      ></Slider>
      <Slider
        color = {"Green"}
        red = {green}
        setRed = {setGreen}
      ></Slider>
      <Slider
        color = {"Blue"}
        red = {blue}
        setRed = {setBlue}
      ></Slider>
      <Box
        red = {red}
        green = {green}
        blue = {blue}
      ></Box>
    </div>
  );
}

export default App;

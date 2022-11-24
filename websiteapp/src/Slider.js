import React from 'react'
import ReactSlider from 'react-slider'
import './App.css';

const Slider = ({color, red, setRed}) => {
  return (
    <ReactSlider
      className="slider"
      thumbClassName={"thumb"+color}
      trackClassName= {"track"+color}
      max={255}
      onChange={(val, index) => setRed(val)}
      renderThumb={(props, state) => <div {...props}>{color + ":" + state.valueNow}</div> }
    />
  )
}

export default Slider
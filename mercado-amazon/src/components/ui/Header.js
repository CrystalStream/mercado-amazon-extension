import React from 'react'
import Logo from '../../assets/img/logo.png'
import utils from '../../utils'

function Header(props) {
  return (
    <div className="header">
      <img src={Logo} alt="Choose the best offer" />
      <div className="pull-right">
        <span>v1.0.0</span>
        <span>with <span role="img" aria-label="love">❤️</span> by <a onClick={() => utils.openTab('https://github.com/CrystalStream') }>CrystalStream</a></span>
      </div>
    </div>
  )
}

export default Header

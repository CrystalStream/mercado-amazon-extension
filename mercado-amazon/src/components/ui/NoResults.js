import React from 'react'
import NotFoundImg from '../../assets/img/not-found.png'

function NoResults() {

  return (
    <div className="no-results-container">
      <img src={NotFoundImg} alt="no products result" />
    </div>
  )
  
}

export default NoResults

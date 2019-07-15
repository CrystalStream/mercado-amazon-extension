import React from 'react'

function Tabs(props) {
  const tabItems = props.titles.map((t, i) => {
    return (
      <li key={i}>
         <a href="#">
          {
            typeof t === 'object' ?
              t :
              <span className="text">{t}</span>
          }
        </a>
      </li>
    )
  })

  return (
    <>
    <div className="tabs is-fullwidth">
      <ul>
        {tabItems}
      </ul>
    </div>
    {
      props.children
    }
    </>
  )
}

export default Tabs

import React from 'react'

function Tabs(props) {
  const tabItems = props.titles.map((t, i) => {
    return (
      <li
        key={i}
        className={props.selectedIndex === i ? 'is-active' : ''}
        onClick={() => { props.onClick(i) }}>
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
    <div className="tabs is-boxed is-fullwidth is-marginless">
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

import React, { useState } from 'react'
import { Product } from '.'
import Tabs from './ui/Tabs'
import Logo from './ui/Logo'
import NoResults from './ui/NoResults'
import Loading from './ui/Loading'

function ProductList(props) {
  const [ selectedIndex, setSelected ] = useState(0)
  const products = props.products[selectedIndex]
  const titles = [
    <Logo to="ml" height="40" width="40" />,
    <Logo to="amazon" height="70" width="70" />
  ]

  function getContent() {
    if (props.isLoading) return <Loading />

    return products && products.length ? 
      <ul>
        {
          products.map((e, i) => {
            return <Product key={i} product={e}/>
          })
        }
        <div id="portal" className="portal" />
      </ul> : <NoResults /> 
  }
  
  return <>
    <Tabs titles={titles} selectedIndex={selectedIndex} onClick={setSelected}>
      <div className="products-container">
      { getContent() }
      </div>
    </Tabs>
  </>
}

export default ProductList

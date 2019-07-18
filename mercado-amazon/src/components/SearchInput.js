import React, { useCallback } from 'react'
import utils from '../utils'

function SearchInput(props) {
  const { criteria, onUpdateProducts, setLoading, isLoading } = props

  const getProducts = useCallback(async () => {
    // don't send again while we are sending
    if (isLoading) return
    // update state
    setLoading(true)
    // send the actual request
    let products = await utils.fetchProducts(criteria)

    if (!products) {
      products = [[], []]
    }
    
    onUpdateProducts(products)
    // once the request is sent, update state again
    setLoading(false)
  }, [isLoading, criteria, setLoading, onUpdateProducts])

  return (
    <>
      <div className="input-search-container">
        <form onSubmit={e => { e.preventDefault(); getProducts() } } noValidate>
          <div className="field">
            <div className={`control ${isLoading ? 'is-loading' : ''}`}>
              <input
                className="input is-rounded"
                type="text"
                placeholder="Type your search and hit 'Enter'"
                onChange={e => props.onChange(e.target.value)}
                value={criteria}
                />
            </div>
          </div>
        </form>
      </div>
    </>
  )
}

export default SearchInput

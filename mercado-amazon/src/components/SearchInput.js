import React, { useState, useCallback } from 'react'
import utils from '../utils'

function SearchInput(props) {
  const [isSending, setIsSending] = useState(false)
  const { criteria, onClick } = props

  const getProducts = useCallback(async () => {
    // don't send again while we are sending
    if (isSending) return
    // update state
    setIsSending(true)
    // send the actual request
    const products = await utils.fetchProducts(criteria)
    onClick(products)
    // once the request is sent, update state again
    setIsSending(false)
  }, [isSending, criteria, onClick])

  return (
    <>
      <div className="input-search-container">
        <form onSubmit={e => { e.preventDefault(); getProducts() } } noValidate>
          <div className="field">
            <div className={`control ${isSending ? 'is-loading' : ''}`}>
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

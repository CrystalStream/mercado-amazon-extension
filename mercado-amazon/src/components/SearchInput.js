import React, { useState, useCallback } from 'react'
import utils from '../utils'

function SearchInput(props) {
  const [isSending, setIsSending] = useState(false)
  const getProducts = useCallback(async () => {
    // don't send again while we are sending
    if (isSending) return
    // update state
    setIsSending(true)
    // send the actual request
    const products = await utils.fetchProducts(props.criteria)
    props.onClick(products)
    // once the request is sent, update state again
    setIsSending(false)
  }, [isSending, props.criteria])

  return (
    <>
      <input onChange={e => props.onChange(e.target.value)} value={props.criteria} />
      <button onClick={getProducts}>Search</button>
    </>
  )
}

export default SearchInput

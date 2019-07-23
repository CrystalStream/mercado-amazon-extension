import React, { useState } from 'react'
import './App.scss'
import { SearchInput, ProductList } from './components'
import Header from './components/ui/Header'

/*global chrome*/

const FIRST_DATA = [
  [
    {
      img: "https://http2.mlstatic.com/reloj-skmei-resistente-al-agua-cronometro-alarma-fecha-1251-D_NQ_NP_603452-MLM31224619114_062019-Q.webp",
      name: "Reloj Skmei Resistente Al Agua Cronómetro Alarma Fecha 1251",
      price: "$269"
    },
    {
      img: "https://http2.mlstatic.com/reloj-metal-led-rosa-negro-plateado-mayoreo-proveedor-D_NQ_NP_724242-MLM31234331523_062019-Q.webp",
      name: "Reloj Metal Led Rosa Negro Plateado Mayoreo Proveedor",
      price: "$79"
    },
    {
      img: "https://http2.mlstatic.com/reloj-metal-led-rosa-negro-plateado-mayoreo-proveedor-D_NQ_NP_785396-MLM31240092727_062019-Q.webp",
      name: "Reloj Metal Led Rosa Negro Plateado Mayoreo Proveedor",
      price: "$69"
    },
    {
      img: "https://http2.mlstatic.com/reloj-led-digital-pantalla-tactil-de-moda-deporte-D_NQ_NP_693327-MLM31226710670_062019-Q.webp",
      name: "Reloj Led Digital Pantalla Tactil De Moda Deporte",
      price: "$39"
    },
    {
      img: "https://m.media-amazon.com/images/I/81o3020+ONL._AC_UL320_.jpg",
      name: "Seiko, Reloj para Hombre SNK809, Acero Inoxidable, Correa Negra",
      price: "$2,004.59"
    },
    {
      img: "https://m.media-amazon.com/images/I/81o3020+ONL._AC_UL320_.jpg",
      name: "Seiko, Reloj para Hombre SNK809, Acero Inoxidable, Correa Negra",
      price: "$2,004.59"
    }
  ],
  [
    {
      img: "https://m.media-amazon.com/images/I/61m9dJ-xvtL._AC_UL320_.jpg",
      name: "WWOOR Últimas Cuarzo Reloj Hombres Analógica de Números Romanos Relojes de Pulsera De Acero Inoxidable Watch Men",
      price: "$589.99"
    },
    {
      img: "https://m.media-amazon.com/images/I/71sczVES08L._AC_UL320_.jpg",
      name: "RORIOS Moda Mujer Relojes de Pulsera Calendario Dial Acero Inoxidable Relojes de Mujer Reloj de Dama",
      price: "$785.00"
    },
    {
      img: "https://m.media-amazon.com/images/I/51p8BKV0WGL._AC_UL320_.jpg",
      name: "WWOOR Clásico Reloj de cuarzo para mujer Round Analog Watch Relojes Resistente al Agua Mujer",
      price: "$518.99"
    },
    {
      img: "https://m.media-amazon.com/images/I/81o3020+ONL._AC_UL320_.jpg",
      name: "Seiko, Reloj para Hombre SNK809, Acero Inoxidable, Correa Negra",
      price: "$2,004.59"
    },
    {
      img: "https://m.media-amazon.com/images/I/51l8TIovftL._AC_UL320_.jpg",
      name: "Seiko, Reloj para Hombre SNK809, Acero Inoxidable, Correa Negra",
      price: "$2,004.59"
    }
  ]
]

function App() {
  const [ searchCriteria, onUpdateCriteria ] = useState('')
  const [ loading, setLoading ] = useState(false)
  const [ products, onUpdateProductList ] = useState([[],[]])

  return (
    <div className="App">
      <div className="container">
        <section className="section is-paddingless">
          <Header />
          <div className="section search-input-container">
            <SearchInput
              onChange={onUpdateCriteria}
              onUpdateProducts={onUpdateProductList}
              criteria={searchCriteria}
              isLoading={loading}
              setLoading={setLoading}
              />
          </div>
          <ProductList products={products} isLoading={loading} />
        </section>
      </div>
    </div>
  )
}

export default App

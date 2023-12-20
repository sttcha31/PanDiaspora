import './globals.css'
import type { Metadata } from 'next'
import { Figtree } from 'next/font/google'
import Navbar from './components/navbar/Navbar'


const font = Figtree({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Pan Diaspora',
  description: 'Mgill Pan Diaspora',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={font.className}>
        <Navbar/>
        <div>
          {children}
        </div>
        
        
      </body>
    </html>
  )
}

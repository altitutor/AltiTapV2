import Head from 'next/head';

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      <Head>
        <title>AltiTap Attendance</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className="bg-[#0c2643] text-white p-4 text-center">
        <h1 className="text-2xl md:text-4xl font-bold">AltiTap</h1>
      </header>

      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="bg-white shadow-md rounded-lg p-4 mb-6">
          <h1 className="text-xl md:text-3xl font-bold text-center mb-4">Welcome to AltiTap Attendance</h1>
          <h2 className="text-lg md:text-2xl text-center mb-4">Mark Your Presence</h2>
        </div>

        <div className="bg-white shadow-md rounded-lg p-4">
          <h2 className="text-lg md:text-2xl font-bold mb-4">Select Your Name:</h2>
          <div className="mb-4">
            <select className="form-select block w-full mt-1 border-gray-300 shadow-sm rounded-md">
              <option>John Doe</option>
              <option>Jane Doe</option>
              <option>Alex Smith</option>
            </select>
          </div>
          <button className="transition-all w-full bg-[#0c2643] hover:bg-[#275182] text-white font-bold py-2 px-4 rounded">
            Submit Attendance
          </button>
        </div>
      </main>

      <footer className="bg-[#0c2643] text-white text-center p-4">
        Designed with ❤ by Altitutor Team
      </footer>
    </div>
  );
}
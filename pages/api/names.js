export default async function handler(req, res) {
    const url = 'https://drive.google.com/uc?export=download&id=1-SOLDxr6tNYquXxnhkZ1GSmA-raTNe-b';
  
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      res.status(200).json(data);
    } catch (error) {
      console.error('Error fetching names:', error);
      res.status(500).json({ error: 'Failed to fetch names' });
    }
  }
  
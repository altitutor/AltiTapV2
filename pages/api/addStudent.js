// pages/api/addStudent.js
import { db } from '../../path/to/your/firebaseConfig';
import { collection, addDoc } from "firebase/firestore"; 

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const docRef = await addDoc(collection(db, "students"), {
        name: req.body.name,
        present: false // Assuming new students are initially not present
      });
      res.status(200).json({ id: docRef.id });
    } catch (e) {
      res.status(400).end();
    }
  } else {
    // Handle any other HTTP methods as needed
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}

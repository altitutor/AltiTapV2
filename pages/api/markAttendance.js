// pages/api/markAttendance.js
import { db } from '../../lib/firebaseConfig'; // Adjust the path as necessary
import { collection, query, where, getDocs, updateDoc, doc } from 'firebase/firestore';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const { name } = req.body; // Extract the name from the request body
      // Query Firestore for a document in the 'students' collection with the matching name
      const studentsCol = collection(db, "students");
      const q = query(studentsCol, where("name", "==", name));
      const querySnapshot = await getDocs(q);

      if (querySnapshot.empty) {
        // If no document found, send a 404 response
        return res.status(404).json({ message: 'Student not found' });
      }

      // Assuming each name is unique and only one document will match
      // Update the 'present' field of the matching document to true
      const studentDoc = querySnapshot.docs[0];
      await updateDoc(doc(db, "students", studentDoc.id), {
        present: true
      });

      // Send a success response
      res.status(200).json({ message: 'Attendance marked successfully' });
    } catch (error) {
      console.error("Error updating attendance:", error);
      res.status(500).json({ error: 'Internal server error' });
    }
  } else {
    // If the request method is not POST, return a 405 Method Not Allowed error
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}

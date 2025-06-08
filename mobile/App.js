import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default function App() {
  const [question, setQuestion] = useState(null);
  const [topic, setTopic] = useState('sumatorias');
  const [message, setMessage] = useState('');

  const fetchQuestion = async () => {
    try {
      const res = await fetch(`http://localhost:8000/generate/${topic}`);
      const data = await res.json();
      setQuestion(data);
    } catch (e) {
      setMessage('Error connecting to backend');
    }
  };

  useEffect(() => {
    fetchQuestion();
  }, [topic]);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Math Champ</Text>
      <Button title="Sumatorias" onPress={() => setTopic('sumatorias')} />
      <Button title="Algebra" onPress={() => setTopic('algebra')} />
      {question && (
        <View style={styles.questionBox}>
          <Text>{question.question}</Text>
          {question.options.map((o, i) => (
            <Button key={i} title={String(o)} onPress={() => setMessage(o === question.answer ? 'Correcto' : 'Incorrecto')} />
          ))}
        </View>
      )}
      <Text>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    fontSize: 24,
    marginBottom: 20,
  },
  questionBox: {
    marginTop: 20,
  },
});

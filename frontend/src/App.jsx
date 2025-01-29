import React from "react";
import { Layout, Card, Row, Col, Table, Carousel } from "antd";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Globe, Plane } from "lucide-react";  
import myImage from './assets/avion.jpg';
import myImage1 from './assets/avion1.jpg';
import myImage2 from './assets/avion2.jpg';
import myImage3 from './assets/avion3.jpg';

import logo from './assets/logo.jpg';  // Ajoute ton logo ici
import Flag from 'react-world-flags';  // Import du package pour les drapeaux

import "antd/dist/reset.css";
import "tailwindcss/tailwind.css";
import "./App.css";  // Assure-toi que ton fichier CSS est bien importé

const { Header, Content, Footer } = Layout;

const flightData = [
  { key: "1", flight: "AF123", origin: "FR", destination: "US", status: "On Time" },
  { key: "2", flight: "BA456", origin: "GB", destination: "JP", status: "Delayed" },
  { key: "3", flight: "LH789", origin: "DE", destination: "AE", status: "Cancelled" },
  { key: "4", flight: "KL101", origin: "NL", destination: "IT", status: "On Time" },
  { key: "5", flight: "UA202", origin: "US", destination: "MX", status: "Delayed" },
  { key: "6", flight: "AF303", origin: "FR", destination: "ES", status: "On Time" },
  { key: "7", flight: "LH404", origin: "DE", destination: "IN", status: "Cancelled" },
  { key: "8", flight: "QF505", origin: "AU", destination: "SG", status: "On Time" },
  { key: "9", flight: "AC606", origin: "CA", destination: "BR", status: "Delayed" },
  { key: "10", flight: "CX707", origin: "HK", destination: "TW", status: "On Time" },
];

const chartData = [
  { name: "Paris", flights: 50 },
  { name: "New York", flights: 40 },
  { name: "Tokyo", flights: 30 },
  { name: "Dubai", flights: 20 },
];

const columns = [
  { title: "Vol", dataIndex: "flight", key: "flight" },
  { 
    title: "Origine", 
    dataIndex: "origin", 
    key: "origin", 
    render: (text) => (
      <>
        <Flag code={text} style={{ width: '20px', height: '20px', marginRight: '8px' }} />
        {text}
      </>
    ) 
  },
  { 
    title: "Destination", 
    dataIndex: "destination", 
    key: "destination", 
    render: (text) => (
      <>
        <Flag code={text} style={{ width: '20px', height: '20px', marginRight: '8px' }} />
        {text}
      </>
    )
  },
  { title: "Statut", dataIndex: "status", key: "status" },
];

// Style pour le carousel
const contentStyle = {
  height: '160px',
  color: '#fff',
  lineHeight: '160px',
  textAlign: 'center',
  background: '#364d79',
};

const App = () => {
  return (
    <Layout className="flex flex-col min-h-screen">
      {/* Header avec logo et titre alignés horizontalement */}
      <Header className="bg-blue-600 text-white text-lg font-bold flex items-center justify-center">
        {/* <img src={logo} alt="Logo" className="w-10 h-10 mr-2" />  Logo à gauche du texte */}
        <h1 className="logo">AIR PLANE ✈️</h1>
      </Header>

      <Content className="flex-grow p-6 bg-gray-100">
        {/* Ajouter des drapeaux à côté des noms des pays */}
        <Row gutter={16} className="mb-6">
          <Col span={8}>
            <Card className="text-center bg-blue-500 text-white " title={<><Flag code="FR" style={{ width: '24px', height: '24px', marginRight: '8px' }} />Paris</>}>
              <h2 className="text-3xl font-bold">1200</h2>
            </Card>
          </Col>
          <Col span={8}>
            <Card className="text-center bg-yellow-500 text-white" title={<><Flag code="US" style={{ width: '24px', height: '24px', marginRight: '8px' }} />New York</>}>
              <h2 className="text-3xl font-bold">85</h2>
            </Card>
          </Col>
        </Row>
        
        {/* Ajout des cartes et graphiques */}
        <Row gutter={16}>
          <Col span={12}>
            <Card title="Statistiques des vols" className="bg-blue-500 text-white">
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={chartData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="flights" fill="#4A90E2" />
                </BarChart>
              </ResponsiveContainer>
            </Card>
          </Col>
          <Col span={12}>
            <Card title="Derniers vols">
              <Table dataSource={flightData} columns={columns} pagination={false} />
            </Card>
          </Col>
        </Row>

        {/* Carousel juste avant le footer */}
     
      </Content>

      {/* Footer avec une touche dorée */}
      <Footer className="text-center bg-blue-600 text-white p-4">
        <span className="text-gold">© 2025 Flight Dashboard</span>
      </Footer>
    </Layout>
  );
};

export default App;

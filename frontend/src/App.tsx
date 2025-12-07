import React, { useState } from 'react';
import { Upload, FileText, CheckCircle, BarChart2 } from 'lucide-react';
import { motion } from 'framer-motion';
import { SkillGraph } from './components/SkillGraph';
import { ATSScore } from './components/ATSScore';

function App() {
  const [file, setFile] = useState<File | null>(null);

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 font-sans">
      <nav className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <FileText className="h-8 w-8 text-blue-600" />
              <span className="ml-2 text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
                Resume AI
              </span>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-16">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-5xl font-extrabold tracking-tight mb-4"
          >
            Optimize Your Resume with <span className="text-blue-600">AI Intelligence</span>
          </motion.h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Parse, Analyze, and Match your resume against top jobs using local LLMs. Privacy-focused, free, and powerful.
          </p>
        </div>

        {/* Upload Section Placeholder */}
        <div className="flex justify-center mb-16">
          <div className="w-full max-w-xl p-8 bg-white rounded-2xl shadow-xl border border-gray-100 hover:border-blue-500 transition-all cursor-pointer group">
            <div className="flex flex-col items-center justify-center border-2 border-dashed border-gray-300 rounded-xl p-10 group-hover:bg-blue-50 transition-colors">
              <Upload className="h-16 w-16 text-blue-400 mb-4 group-hover:scale-110 transition-transform" />
              <p className="text-lg font-medium text-gray-700">Drag & Drop your resume here</p>
              <p className="text-sm text-gray-500 mt-2">PDF or DOCX (Max 10MB)</p>
            </div>
          </div>
        </div>

        {/* Dashboard Preview */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100">
            <h3 className="text-xl font-bold mb-4 flex items-center">
              <BarChart2 className="w-5 h-5 mr-2 text-blue-600" />
              Skill Gap Visualization
            </h3>
            <SkillGraph />
          </div>

          <div className="flex flex-col gap-6">
            <ATSScore score={85} />
            <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100 flex-grow">
              <h3 className="text-xl font-bold mb-4 flex items-center">
                <CheckCircle className="w-5 h-5 mr-2 text-green-500" />
                AI Suggestions
              </h3>
              <ul className="space-y-3">
                <li className="flex items-start text-sm text-gray-600">
                  <div className="w-2 h-2 rounded-full bg-blue-500 mt-1.5 mr-2 flex-shrink-0" />
                  Add "Docker" to Skills section (found in Job Description).
                </li>
                <li className="flex items-start text-sm text-gray-600">
                  <div className="w-2 h-2 rounded-full bg-blue-500 mt-1.5 mr-2 flex-shrink-0" />
                  Quantify your impact at Company X (e.g., "Improved speed by 20%").
                </li>
                <li className="flex items-start text-sm text-gray-600">
                  <div className="w-2 h-2 rounded-full bg-blue-500 mt-1.5 mr-2 flex-shrink-0" />
                  Use active voice in bullet points.
                </li>
              </ul>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;

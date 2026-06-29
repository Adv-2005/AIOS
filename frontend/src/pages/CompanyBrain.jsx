import { useState } from "react";
import { askQuestion, uploadDocument } from "../api/companyBrain";


export default function CompanyBrain() {

    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");

    const [sources, setSources] = useState([]);

    const [loading, setLoading] = useState(false);
    
    const [selectedFile, setSelectedFile] = useState(null);

    const [uploading, setUploading] = useState(false);

    async function handleAsk() {

        if (!question.trim()) return;

        setLoading(true);

        try {

            const data = await askQuestion(question);

            setAnswer(data.answer);

            setSources(data.sources);

        } catch (err) {

            console.error(err);

            alert("Failed to get response.");

        }

        setLoading(false);

    }
    async function handleUpload() {

    if (!selectedFile) return;

    setUploading(true);

    try {

        const data = await uploadDocument(selectedFile);

        alert(`Document uploaded successfully.\nID: ${data.document_id}`);

        setSelectedFile(null);

    } catch (err) {

        console.error(err);

        alert("Upload failed.");

    }

    setUploading(false);

}

    return (


        <div className="space-y-6">

            <h1 className="text-3xl font-bold">

                Company Brain

            </h1>
            <div className="border rounded p-4 bg-white space-y-4">

    <h2 className="text-xl font-semibold">

        Upload PDF

    </h2>

    <input

        type="file"

        accept=".pdf"

        onChange={(e) => setSelectedFile(e.target.files[0])}

    />

    <button

        className="border rounded px-4 py-2"

        onClick={handleUpload}

    >

        {uploading ? "Uploading..." : "Upload"}

    </button>

</div>

            <textarea

                className="border rounded p-3 w-full"

                rows={4}

                placeholder="Ask a question..."

                value={question}

                onChange={(e) => setQuestion(e.target.value)}

            />

            <button

                className="border px-4 py-2 rounded"

                onClick={handleAsk}

            >

                {loading ? "Thinking..." : "Ask"}

            </button>

            {answer && (

                <div className="border rounded p-4 bg-white">

                    <h2 className="font-semibold mb-2">

                        Answer

                    </h2>

                    <p>

                        {answer}

                    </p>

                </div>

            )}

            {sources.length > 0 && (

                <div className="border rounded p-4 bg-white">

                    <h2 className="font-semibold mb-2">

                        Sources

                    </h2>

                    <ul>

                        {sources.map((source, index) => (

                            <li key={index}>

                                {source}

                            </li>

                        ))}

                    </ul>

                </div>

            )}

        </div>

    );

}


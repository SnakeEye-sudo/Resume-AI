import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Sphere } from '@react-three/drei';

function AnimatedSphere() {
    const meshRef = useRef<THREE.Mesh>(null);

    useFrame((state, delta) => {
        if (meshRef.current) {
            meshRef.current.rotation.x += delta * 0.2;
            meshRef.current.rotation.y += delta * 0.5;
        }
    });

    return (
        <Sphere ref={meshRef} args={[1, 32, 32]}>
            <meshStandardMaterial color="#3b82f6" wireframe />
        </Sphere>
    );
}

export function SkillGraph() {
    return (
        <div className="h-64 w-full bg-slate-900 rounded-xl overflow-hidden shadow-inner">
            <Canvas camera={{ position: [0, 0, 3] }}>
                <ambientLight intensity={0.5} />
                <pointLight position={[10, 10, 10]} />
                <AnimatedSphere />
                <OrbitControls enableZoom={false} />
            </Canvas>
        </div>
    );
}
